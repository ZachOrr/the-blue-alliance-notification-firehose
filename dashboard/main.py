import json
import logging
import os

import google.cloud.logging
from dotenv import load_dotenv
from flask import Flask, render_template, Response

from shared.ndb import create_ndb_client, ndb_wsgi_middleware
from shared.notification import Notification

load_dotenv()


_project = os.environ.get("GOOGLE_CLOUD_PROJECT")
_is_local = os.environ.get("GAE_ENV") in (None, "localdev")

if not _is_local:
    logging_client = google.cloud.logging.Client(project=_project)
    logging_client.setup_logging()

client = create_ndb_client(readonly=True)

app = Flask(__name__)
app.wsgi_app = ndb_wsgi_middleware(client, app.wsgi_app)


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=_is_local)
