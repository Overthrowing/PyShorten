from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Url(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.Text)
	shortened_url = db.Column(db.Text)
	times_visited = db.Column(db.Integer)
	date = db.Column(db.DateTime(timezone=True), default=func.now())
