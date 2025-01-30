from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    is_done = db.Column(db.Boolean, default=False)

class User(db.Model, UserMixin):
    __tablename__ = "users" 

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(700), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    tasks = db.relationship('Task', backref='owner', lazy=True) 
