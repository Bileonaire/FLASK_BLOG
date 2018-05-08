"""handles database models"""
# pylint: disable=E1101
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Blogpost(db.Model):
    """Creates model for blogposts in the database"""


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    subtitle = db.Column(db.String(100))
    author = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)
