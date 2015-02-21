from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from dev import routes, models