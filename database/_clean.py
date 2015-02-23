"""
Filename: _clean.py
From: Brian Soe
Description: Remove all created databases.
"""

import subprocess

subprocess.call(['rm','-rf','repo'])
subprocess.call(['rm','-rf','table.db'])