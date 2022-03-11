from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class ContactUs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emailid = db.Column(db.String(150))
    fname = db.Column(db.String(150))
    lname = db.Column(db.String(150))
    mobnum = db.Column(db.String(10))
    message = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    cellnum = db.Column(db.Numeric(10))
