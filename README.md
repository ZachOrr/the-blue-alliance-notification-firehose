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

Deploy the app

```
$ gcloud app deploy
```