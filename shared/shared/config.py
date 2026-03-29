import os

from dotenv import load_dotenv

load_dotenv()

project = os.environ.get("GOOGLE_CLOUD_PROJECT")
is_local = os.environ.get("GAE_ENV") in (None, "localdev")


def setup_logging():
    """Set up Google Cloud logging in production environments."""
    if not is_local:
        import google.cloud.logging

        logging_client = google.cloud.logging.Client(project=project)
        logging_client.setup_logging()
