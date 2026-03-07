# TBA Notification Firehose

This is a simple, demo webapp for receiving webhooks from The Blue Alliance. It has been subscribed to the 'firehose' key, so it will receive notifications for all events this year.

Demo app: http://tba-notification-firehose.appspot.com/

Styling provided by [Bootstrap Material Design](http://fezvrasta.github.io/bootstrap-material-design)

## Running Locally

Make sure you have the [gcloud cli](https://cloud.google.com/sdk/docs/install) installed.

Follow the instructions to install the [Datastore emulator](https://cloud.google.com/datastore/docs/tools/datastore-emulator).

The instructions are a little wonky in the links above, so here's directions for getting the Datastore emulator running on Linux/macOS. YMMV.

Start the datastore emulator (install the emulator if it is not already installed)

```
gcloud beta emulators datastore start
```

You should see a `Dev App Server is now running.` message indicating the server has started.

In another terminal session (we will run our app in this session) setup the required environment variables

```
$(gcloud beta emulators datastore env-init)
```

You can confirm the variables are setup -

```
echo $DATASTORE_EMULATOR_HOST
> localhost:8081
```

Run the app

```
$ python main.py
```

A tool like ngrok can be used to point the production TBA website at your local instance to test webhooks. Alternatively you can setup a local instance of TBA to test webhooks against your local firehose instance. Both of these are left as an exercise to the reader.

## Deploying

Create a project

```
$ gcloud projects create PROJECT_ID
```

or if you have an existing project

```
$ gcloud config set project PROJECT_ID
```

You will likely have to [enable billing](https://cloud.google.com/billing/docs/how-to/modify-project) for your project.

### Secrets Setup

This app uses [Google Cloud Secret Manager](https://cloud.google.com/secret-manager) to store the TBA webhook secret.

For local development, create a `.env` file with your TBA webhook secret:

```
$ echo 'TBA_SECRET=YOUR_TBA_SECRET' > .env
```

For production, enable the Secret Manager API:

```
$ gcloud services enable secretmanager.googleapis.com --project=PROJECT_ID
```

Create the secret with your TBA webhook secret value:

```
$ echo -n "YOUR_TBA_SECRET" | gcloud secrets create TBA_SECRET --data-file=- --project=PROJECT_ID
```

Grant your App Engine service account access to read the secret:

```
$ gcloud secrets add-iam-policy-binding TBA_SECRET \
    --member="serviceAccount:PROJECT_ID@appspot.gserviceaccount.com" \
    --role="roles/secretmanager.secretAccessor" \
    --project=PROJECT_ID
```

### Deploy

Deploy the app

```
$ gcloud app deploy
```

### Continuous Deployment (GitHub Actions)

This repo includes a GitHub Actions workflow that auto-deploys to App Engine on every push to `main`.

Create a service account and download a JSON key:

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
