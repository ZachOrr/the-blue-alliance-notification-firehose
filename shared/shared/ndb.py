import os

import google.auth
from google.cloud import ndb


def create_ndb_client(*, readonly=False):
    """Create an ndb Client configured for the current environment.

    In production, uses default credentials. Locally, uses the Datastore emulator
    if DATASTORE_EMULATOR_HOST is set, otherwise falls back to application-default
    credentials with an appropriate scope.
    """
    project = os.environ.get("GOOGLE_CLOUD_PROJECT")
    is_local = os.environ.get("GAE_ENV") in (None, "localdev")

    if not is_local:
        return ndb.Client(project=project)

    if os.environ.get("DATASTORE_EMULATOR_HOST") is not None:
        from google.auth.credentials import AnonymousCredentials

        return ndb.Client(project=project, credentials=AnonymousCredentials())

    scope = (
        "https://www.googleapis.com/auth/datastore.readonly"
        if readonly
        else "https://www.googleapis.com/auth/datastore"
    )
    credentials, _ = google.auth.default(scopes=[scope])
    return ndb.Client(project=project, credentials=credentials)


def ndb_wsgi_middleware(ndb_client, wsgi_app):
    """Wrap a WSGI app so every request runs inside an ndb context."""

    def middleware(environ, start_response):
        with ndb_client.context():
            iterator = wsgi_app(environ, start_response)
            try:
                yield from iterator
            finally:
                if hasattr(iterator, "close"):
                    iterator.close()

    return middleware
