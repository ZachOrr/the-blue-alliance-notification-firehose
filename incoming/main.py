import hashlib
import hmac
import json
import logging
import os

import google.cloud.logging
from dotenv import load_dotenv
from flask import Flask, Response, request

from shared.ndb import create_ndb_client, ndb_wsgi_middleware
from shared.notification import Notification
from shared.secrets import get_secret

load_dotenv()


SECRET = get_secret("TBA_SECRET")

_project = os.environ.get("GOOGLE_CLOUD_PROJECT")
_is_local = os.environ.get("GAE_ENV") in (None, "localdev")

if not _is_local:
    logging_client = google.cloud.logging.Client(project=_project)
    logging_client.setup_logging()

client = create_ndb_client()

app = Flask(__name__)
app.wsgi_app = ndb_wsgi_middleware(client, app.wsgi_app)


@app.route("/incoming", methods=["POST"])
def incoming():
    checksum = request.headers.get("X-TBA-HMAC")
    if not checksum:
        return Response(status=400)

    payload = request.data.decode("utf-8")

    try:
        json_payload = request.get_json()
        if json_payload["message_type"] == "verification":
            verification_key = json_payload["message_data"]["verification_key"]
            logging.info(f"Verification key: {verification_key}")
            return Response(status=200)
    except Exception:
        pass

    local_checksum = hmac.new(
        SECRET.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256
    ).hexdigest()

    if local_checksum != checksum:
        return Response(status=400)

    Notification(payload=payload).put()

    return Response(status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=_is_local)
