import hashlib
import hmac
import logging

from flask import Flask, Response, request

from shared.config import is_local, setup_logging
from shared.ndb import create_ndb_client, ndb_wsgi_middleware
from shared.notification import Notification
from shared.secrets import get_secret

SECRET = get_secret("TBA_SECRET")

setup_logging()

client = create_ndb_client()

app = Flask(__name__)
app.wsgi_app = ndb_wsgi_middleware(client, app.wsgi_app)


@app.route("/incoming", methods=["POST"])
def incoming() -> Response:
    checksum = request.headers.get("X-TBA-HMAC")
    if not checksum:
        return Response(status=400)

    payload = request.data.decode("utf-8")

    local_checksum = hmac.new(
        SECRET.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256
    ).hexdigest()
    if not hmac.compare_digest(local_checksum, checksum):
        return Response(status=400)

    json_payload = request.get_json(silent=True) or {}
    message_type = json_payload.get("message_type")

    if message_type == "verification":
        verification_key = json_payload.get("message_data", {}).get("verification_key")
        if verification_key:
            logging.info(f"Verification key: {verification_key}")
        return Response(status=200)

    Notification(payload=payload).put()

    return Response(status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=is_local)
