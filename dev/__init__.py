from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import sys
import random

selection = '0123456789abcdefghijklmnopqrstuvwxyz'

app = Flask(__name__, static_url_path='')
app.config.from_object('config')
app.secret_key = ''
for i in range(50):
    index = random.randint(0,len(selection)-1)
    app.secret_key += selection[index]
db = SQLAlchemy(app)

from dev import routes, models