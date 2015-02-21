"""
Filename: server.py
Author: Brian Soe
Description: Activates server for Flask application.
"""

from dev import app, routes
app.run(debug=True)
