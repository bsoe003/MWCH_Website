"""
Filename: server.py
Author: Brian Soe
Description: Activates server for Flask application.
"""

from dev import app, routes
import os

port = int(os.environ.get('PORT', 5000))
app.run(port=port, debug=True)                                      