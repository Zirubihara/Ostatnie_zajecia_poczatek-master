from sqla_wrapper import SQLAlchemy
import os

db = SQLAlchemy(os.getenv("DATEBASE_URL", "sqlite:///localhost.sqlite"))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    second_name = db.Column(db.String)
    phone_number = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    session_token = db.Column(db.String)