"""contains configuration variables"""
from os import getenv

DEBUG = True
SECRET_KEY = getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = True
