"""
Filename: config.py
Author: Brian Soe
Description: Configuration setting for Flask application.
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database/table.db')
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'database/repo')

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'mwch.test001@gmail.com'
MAIL_PASSWORD = 'hawtlinks'