# TBA Notification Firehose

A webapp for receiving and monitoring webhooks from The Blue Alliance. Subscribed to the 'firehose' key, so it receives notifications for all events this year.

Demo app: http://tba-notification-firehose.appspot.com/

## Architecture

The app is split into two GAE services:

- **`dashboard/`** (Python) — Read-only web UI for viewing recent notifications. Default service.
- **`incoming/`** (Python) — Lightweight webhook receiver that validates HMAC signatures and writes to Datastore.
- **`shared/`** — Shared Python package containing the `Notification` model, ndb helpers, and secret loading used by both services.

A `dispatch.yaml` routes `/incoming` requests to the incoming service; everything else is handled by the dashboard.

## Setup

### GCP Project

Create a project or use an existing one:

```
$ gcloud projects create PROJECT_ID
$ gcloud config set project PROJECT_ID
```

You will likely have to [enable billing](https://cloud.google.com/billing/docs/how-to/modify-project) for your project.

### `.env` file

Create a `.env` file in the repo root with your secrets:

```
TBA_SECRET=YOUR_TBA_SECRET
GOOGLE_CLOUD_PROJECT=PROJECT_ID
```

For local development, the app reads secrets from `.env` first, falling back to Secret Manager in production.

## Running Locally

### Docker (both services)

Run both the dashboard and incoming services locally via Docker Compose with a Datastore emulator:

```
$ make docker-up
```

This starts three containers: a Datastore emulator, the Flask dashboard, and the Flask incoming service.

- Dashboard: http://localhost:8080
- Incoming webhook: http://localhost:8081/incoming
- Datastore emulator: http://localhost:8432

Source files are volume-mounted, so changes are reflected immediately (restart the container to pick them up).

To stop: `make docker-down` or <kbd>Ctrl+C</kbd>.

### Dashboard only (no Docker)

The dashboard can also run standalone against your GCP project's Datastore in read-only mode:

```
$ gcloud auth application-default login
$ make run
```

The dashboard will be available at http://localhost:8080.

## Deploying

### Secrets Setup

Enable the Secret Manager API:

```
$ gcloud services enable secretmanager.googleapis.com --project=PROJECT_ID
```

Create secrets with your values:

```
$ echo -n "YOUR_TBA_SECRET" | gcloud secrets create TBA_SECRET --data-file=- --project=PROJECT_ID
```

Grant your App Engine service account access:

```
$ gcloud secrets add-iam-policy-binding TBA_SECRET \
    --member="serviceAccount:PROJECT_ID@appspot.gserviceaccount.com" \
    --role="roles/secretmanager.secretAccessor" \
    --project=PROJECT_ID
```

### Deploy

```
$ gcloud app deploy dashboard/app.yaml incoming/app.yaml dispatch.yaml
```

### Continuous Deployment (GitHub Actions)

This repo includes a GitHub Actions workflow that auto-deploys to App Engine on every push to `master`.

Enable the App Engine Admin API:

```
$ gcloud services enable appengine.googleapis.com --project=PROJECT_ID
```

Create a service account, grant it the necessary roles, and download a JSON key:

```
$ gcloud iam service-accounts create github-deploy \
    --display-name="GitHub Deploy" \
    --project=PROJECT_ID

$ gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:github-deploy@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/appengine.deployer"

$ gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:github-deploy@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/appengine.serviceAdmin"

$ gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:github-deploy@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/cloudbuild.builds.builder"

$ gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:github-deploy@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/storage.admin"

$ gcloud iam service-accounts add-iam-policy-binding \
    PROJECT_ID@appspot.gserviceaccount.com \
    --member="serviceAccount:github-deploy@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountUser" \
    --project=PROJECT_ID

$ gcloud iam service-accounts keys create key.json \
    --iam-account=github-deploy@PROJECT_ID.iam.gserviceaccount.com
```

Set these two secrets in your GitHub repo (Settings → Secrets and variables → Actions):

| Secret | Value |
|---|---|
| `GCLOUD_AUTH` | Contents of the `key.json` file |
| `GCLOUD_PROJECT_ID` | Your GCP project ID |

After setting the secrets, delete the local key file:

```
$ rm key.json
```
