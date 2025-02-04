from mongoengine import Document, StringField, BooleanField, DateTimeField, ReferenceField, EmailField
from flask_login import UserMixin
import datetime

class User(Document, UserMixin):
    meta = {'collection': 'users'}  # MongoDB collection name
    email = EmailField(unique=True, required=True)
    password = StringField(required=True, max_length=700)
    first_name = StringField(required=True, max_length=150)

class Task(Document):
    meta = {'collection': 'tasks'}  # MongoDB collection name
    text = StringField(max_length=10000)
    date = DateTimeField(default=datetime.datetime.utcnow)
    user = ReferenceField(User, required=True, reverse_delete_rule=2)  # Reference to User
    is_done = BooleanField(default=False)