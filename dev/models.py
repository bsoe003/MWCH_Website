"""
Filename: models.py
Author: Brian Soe
Description: Model schema for database.
Prerequisite: Flask server must be running.
"""
from dev import db

class Stories(db.Model):
    """ DB schema model for Stories """
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    text = db.Column(db.Text)
    approval = db.Column(db.Boolean)

    def __repr__(self):
        """ default representation of Stories object """
        result ='Entry #%s\nDate: %s\nApproved: %s\n\n%s' \
            % (str(self.id),str(self.date),str(self.approval),str(self.text))
        return result

    def __str__(self):
        """ string form of Stories object """
        return str(self.__repr__)