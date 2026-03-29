import os

from google.cloud import secretmanager

from shared.config import project


def get_secret(secret_id):
    """Load a secret from GCP Secret Manager, falling back to environment variables for local dev."""
    if os.environ.get(secret_id):
        return os.environ[secret_id]
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project}/secrets/{secret_id}/versions/latest"
    return client.access_secret_version(name=name).payload.data.decode("utf-8")
