"""
Filename: server.py
Author: Brian Soe
Description: Activates server for Flask application.
"""

from dev import app, routes
import os
import sys

port = int(os.environ.get('PORT', 5000))
try:
	app.run(host=sys.argv[1], port=port, debug=True)
except:
    app.run(port=port, debug=True)