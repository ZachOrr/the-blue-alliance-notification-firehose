import json

from flask import Flask, render_template, Response

from shared.config import is_local, setup_logging
from shared.ndb import create_ndb_client, ndb_wsgi_middleware
from shared.notification import Notification

setup_logging()

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
    app.run(host="0.0.0.0", port=8080, debug=is_local)
