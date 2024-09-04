from .database import db
import datetime

class WebhookEvent(db.Document):
    req_id = db.StringField(required=True, unique=True)
    event_type = db.StringField(required=True)
    author = db.StringField(required=True)
    from_branch = db.StringField()
    to_branch = db.StringField(required=True)
    timestamp = db.DateTimeField(default=datetime.datetime.utcnow)
