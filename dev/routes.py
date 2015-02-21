"""
Filename: routes.py
Author: Brian Soe
Description: List and defines all functionality of routes.
Prerequisite: Flask server must be running.
"""

from dev import app
from flask import request, redirect, render_template

@app.route('/')
def viewIndex():
    return render_template('index.html')

@app.route('/about')
def viewAbout():
    return redirect('/about/background')

@app.route('/about/background')
def viewBackground():
    return 'Background & History'

@app.route('/about/muiristas')
def viewMuiristas():
    return 'Muiristas'

@app.route('/about/sources')
def viewSources():
    return 'Where We Source From'

@app.route('/menu')
def viewMenu():
    return redirect('/menu/regular')

@app.route('/menu/regular')
def viewRegular():
    return 'Regular Drinks'

@app.route('/menu/blended_iced')
def viewBlended():
    return 'Blended & Iced Drinks'

@app.route('/menu/pastries')
def viewPastries():
    return 'Pastries'

@app.route('/stories')
def viewStories():
    return 'Stories'

@app.route('/gallery')
def viewGallery():
    return 'Gallery'

@app.route('/submit', methods=['POST'])
def submit():
    text = request.args.get('q')
    print text
    return 'Permission Denied'
