"""
Filename: server.py
Author: Brian Soe
Description: Activates server for Flask application.
"""

from dev import app, routes
import os

#app.run(debug=True) # debug on for constant update upon change
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)                                      