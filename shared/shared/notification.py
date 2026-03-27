from google.cloud import ndb


class Notification(ndb.Model):
    payload = ndb.TextProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
