from datetime import datetime

from mongoengine import Document, DateTimeField, StringField, ObjectIdField


class User(Document):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    # created_at = DateTimeField(default=datetime.now())
