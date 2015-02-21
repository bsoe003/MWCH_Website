"""
Filename: models.py
Author: Brian Soe
Description: Model schema for database.
Prerequisite: Flask server must be running.
"""
from dev import db

class Stories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Time)
    text = db.Column(db.Text)
    approval = db.Column(db.Boolean)

    def __str__(self):
        result ='Entry #%s\nDate: %s\nApproved: %s\n\n%s' \
            % (str(self.id),str(self.date),str(self.approval),str(text))
        return result