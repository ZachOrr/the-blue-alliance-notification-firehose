import json
import os
from datetime import timezone
from typing import List, Optional

from flask import Flask, jsonify, request, send_from_directory

from shared.config import is_local, setup_logging
from shared.ndb import create_ndb_client, ndb_wsgi_middleware
from shared.notification import Notification

setup_logging()

client = create_ndb_client(readonly=True)

app = Flask(__name__)
app.wsgi_app = ndb_wsgi_middleware(client, app.wsgi_app)


def get_notification_type_from_payload(payload: dict) -> Optional[str]:
    """Extract notification type from the TBA webhook payload."""
    return payload.get("message_type")


def get_all_notifications(limit: int = 100) -> List[dict]:
    """Fetch notifications from Datastore, ordered by most recent first."""
    notifications = Notification.query().order(-Notification.created).fetch(limit)

    result = []
    for notification in notifications:
        try:
            payload = json.loads(notification.payload)
        except (json.JSONDecodeError, TypeError):
            payload = {"error": "Failed to parse payload"}

        notification_type = get_notification_type_from_payload(payload)

        created = notification.created
        # Datastore/NDB can return naive UTC datetimes; make UTC explicit for clients.
        if created.tzinfo is None:
            created = created.replace(tzinfo=timezone.utc)
        timestamp = created.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")

        result.append(
            {
                "id": notification.key.id(),
                "timestamp": timestamp,
                "type": notification_type or "unknown",
                "payload": payload,
            }
        )

    return result


def filter_notifications_by_type(
    notifications: List[dict], types: List[str]
) -> List[dict]:
    """Filter notifications by type."""
    if not types:
        return notifications

    return [n for n in notifications if n.get("type") in types]


@app.route("/api/notifications")
def api_notifications():
    """API endpoint for fetching notifications with optional filtering by type."""
    # Get optional types query parameter (comma-separated)
    types_param = request.args.get("types", "")
    types = (
        [t.strip() for t in types_param.split(",") if t.strip()] if types_param else []
    )

    # Fetch all notifications
    notifications = get_all_notifications(limit=100)

    # Filter by type if specified
    if types:
        notifications = filter_notifications_by_type(notifications, types)

    return jsonify({"notifications": notifications})


BUILD_DIR = os.path.join(os.path.dirname(__file__), "static", "build")


@app.route("/")
def root():
    """Serve the React SPA index.html."""
    index_path = os.path.join(BUILD_DIR, "index.html")

    if os.path.exists(index_path):
        return send_from_directory(BUILD_DIR, "index.html")

    return {
        "error": "React app not built",
        "message": "Run 'make build-dashboard' first.",
    }, 503


@app.route("/<path:filename>")
def serve_static(filename):
    """Serve static assets from the React build directory."""
    file_path = os.path.join(BUILD_DIR, filename)
    if os.path.exists(file_path):
        return send_from_directory(BUILD_DIR, filename)
    # Fall back to index.html for SPA client-side routing
    return send_from_directory(BUILD_DIR, "index.html")


@app.route("/webhooks")
def webhooks():
    """Legacy endpoint for webhook notifications."""
    notifications = Notification.query().order(-Notification.created).fetch(100)
    notifications = [
        {"time": str(n.created), "payload": json.loads(n.payload)}
        for n in notifications
    ]
    return notifications


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=is_local)
