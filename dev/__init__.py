"""
Filename: __init__.py
Author: Brian Soe
Description: Activates Flask application and send to server.py.
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
import sys
import random
import subprocess

# secret key selection characters
selection = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

app = Flask(__name__, static_url_path='') # open flask
app.config.from_object('config') # map configuration to config.py

# generate secret key. random every time server runs
app.secret_key = ''
for i in range(50):
    index = random.randint(0,len(selection)-1)
    app.secret_key += selection[index]

# activate database and mail components
db = SQLAlchemy(app)
mail = Mail(app)

# hacky way to compile sass
path = "dev/static/"
subprocess.call(['sass',path+'scss/base.scss',path+'css/style.css'])

from dev import routes, models