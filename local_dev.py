"""Minimal local dev server with mock data to test UI changes without GCP dependencies."""
import json
from flask import Flask, render_template

app = Flask(__name__)

MOCK_NOTIFICATIONS = [
    {
        "time": "2026-03-07 18:39:54",
        "payload": {
            "message_type": "match_video",
            "message_data": {
                "event_name": "FIM District Mt Pleasant Event presented by AT&T",
                "match": {
                    "key": "2026mimtp_qm12",
                    "event_key": "2026mimtp",
                    "videos": [{"type": "youtube", "key": "Cvss0eqqflc"}],
                    "alliances": {
                        "red": {"team_keys": ["frc1", "frc2", "frc3"], "score": 50},
                        "blue": {"team_keys": ["frc4", "frc5", "frc6"], "score": 60},
                    },
                },
            },
        },
    },
    {
        "time": "2026-03-07 18:38:50",
        "payload": {
            "message_type": "upcoming_match",
            "message_data": {
                "event_name": "FIM District Mt Pleasant Event presented by AT&T",
                "match_key": "2026mimtp_qm14",
                "team_keys": ["frc2337", "frc9568", "frc9673", "frc4381", "frc3655", "frc3688"],
            },
        },
    },
    {
        "time": "2026-03-07 18:38:54",
        "payload": {
            "message_type": "match_score",
            "message_data": {
                "event_name": "FIM District Mt Pleasant Event presented by AT&T",
                "match": {
                    "key": "2026mimtp_qm12",
                    "event_key": "2026mimtp",
                    "alliances": {
                        "red": {"team_keys": ["frc10614", "frc9594", "frc5234"], "score": 44},
                        "blue": {"team_keys": ["frc5436", "frc5110", "frc2405"], "score": 98},
                    },
                },
            },
        },
    },
    {
        "time": "2026-03-07 18:38:50",
        "payload": {
            "message_type": "upcoming_match",
            "message_data": {
                "event_name": "FMA District Warren Hills Event",
                "match_key": "2026njwas_qm38",
                "team_keys": ["frc41", "frc6945", "frc8117", "frc6016", "frc8771", "frc9116"],
            },
        },
    },
    {
        "time": "2026-03-07 18:38:42",
        "payload": {
            "message_type": "schedule_updated",
            "message_data": {
                "event_name": "FMA District Warren Hills Event",
                "event_key": "2026njwas",
            },
        },
    },
    {
        "time": "2026-03-07 18:37:00",
        "payload": {
            "message_type": "ping",
            "message_data": {
                "title": "Test Ping",
                "desc": "This is a test ping notification.",
            },
        },
    },
]


@app.route("/")
def root():
    return render_template(
        "notification_list_material.html",
        notifications_json=json.dumps(MOCK_NOTIFICATIONS),
    )


if __name__ == "__main__":
    app.run(port=8080, debug=True)
