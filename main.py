import json
import logging

import google.cloud.logging
from flask import Flask, render_template, request, Response
from google.cloud import ndb

from models.notification import Notification


SECRET = "REPLACE_WITH_SECRET"

logging_client = google.cloud.logging.Client()
logging_client.setup_logging()

client = ndb.Client()


def ndb_wsgi_middleware(wsgi_app):
    def middleware(environ, start_response):
        with client.context():
            return wsgi_app(environ, start_response)

    return middleware


app = Flask(__name__)
app.wsgi_app = ndb_wsgi_middleware(app.wsgi_app)


@app.route("/")
def root():
    notifications = Notification.query().order(-Notification.created).fetch(100)
    notifications = [
        {"time": str(n.created), "payload": json.loads(n.payload)}
        for n in notifications
    ]
    return render_template(
        "notification_list_material.html", notifications_json=json.dumps(notifications)
    )


@app.route("/webhooks")
def webhooks():
    notifications = Notification.query().order(-Notification.created).fetch(100)
    notifications = [
        {"time": str(n.created), "payload": json.loads(n.payload)}
        for n in notifications
    ]
    return notifications


@app.route("/incoming", methods=["POST"])
def incoming():
    checksum = request.headers["X-TBA-HMAC"]
    payload = request.data.decode("utf-8")

    import hashlib, hmac

    try:
        json_payload = request.get_json()
        if json_payload["message_type"] == "verification":
            verification_key = json_payload["message_data"]["verification_key"]
            logging.info(f"Verification key: {verification_key}")
            return Response(status=200)
    except:
        pass

    local_checksum = hmac.new(
        SECRET.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256
    ).hexdigest()

    if local_checksum != checksum:
        return Response(status=400)

    Notification(payload=payload).put()

    return Response(status=200)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
