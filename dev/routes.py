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
    #return app.send_static_file('index.html')
    return render_template('index.html', level=0)

@app.route('/about')
def viewAbout():
    return redirect('/about/background')

@app.route('/about/background')
def viewBackground():
    return render_template('about/background.html', level=1)

@app.route('/about/muiristas')
def viewMuiristas():
    return render_template('about/muiristas.html', level=1)

@app.route('/about/sources')
def viewSources():
    return render_template('about/sources.html', level=1)

@app.route('/menu')
def viewMenu():
    return redirect('/menu/regular')

@app.route('/menu/regular')
def viewRegular():
    return render_template('menu/regular.html', level=1)

@app.route('/menu/blended_iced')
def viewBlended():
    return render_template('menu/blended.html', level=1)

@app.route('/menu/pastries')
def viewPastries():
    return render_template('menu/pastries.html', level=1)

@app.route('/stories')
def viewStories():
    return render_template('stories.html', level=0)

@app.route('/gallery')
def viewGallery():
    return render_template('gallery.html', level=0)

@app.route('/sample')
def viewSample():
    return render_template('sample.html', level=0)

@app.route('/submit', methods=['POST'])
def submit():
    text = request.args.get('q')
    print text
    return 'Permission Denied'
