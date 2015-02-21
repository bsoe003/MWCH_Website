"""
Filename: routes.py
Author: Brian Soe
Description: List and defines all functionality of routes.
Prerequisite: Flask server must be running.
"""

from dev import app, db, models, loader
from flask import request, redirect, url_for
from datetime import datetime

@app.route('/')
def viewIndex():
    return render_template('index.html', level=0)

@app.route('/about')
def viewAbout():
    return redirect('/about/background')

@app.route('/about/background')
def viewBackground():
    return render_template('about/background.html', level=1)

@app.route('/about/muiristas')
def viewMuiristas():
    data = loader.load('about_muiristas.csv')
    return render_template('about/muiristas.html', 
        level=1,
        muiristas=data)

@app.route('/about/sources')
def viewSources():
    return render_template('about/sources.html', level=1)

@app.route('/menu')
def viewMenu():
    return redirect('/menu/regular')

@app.route('/menu/regular')
def viewRegular():
    data = loader.load('menu_regular.csv')
    return render_template('menu/regular.html', 
        level=1,
        menu=data)

@app.route('/menu/blended_iced')
def viewBlended():
    data = loader.load('menu_blended.csv')
    return render_template('menu/blended.html', 
        level=1,
        menu=data)

@app.route('/menu/pastries')
def viewPastries():
    data = loader.load('menu_pastries.csv')
    return render_template('menu/pastries.html', 
        level=1,
        menu=data)

@app.route('/stories')
def viewStories():
    return render_template('stories.html', level=0)

@app.route('/gallery')
def viewGallery():
    data = loader.load('gallery_photos.csv')
    return render_template('gallery.html',
        level=0,
        gallery=data)

@app.route('/sample')
def viewSample():
    return render_template('sample.html', level=0)

@app.route('/submit', methods=['POST'])
def submit():
    text = request.args.get('q')
    story = models.Stories(date=datetime.now(), text=text, approval=False)
    db.session.add(story)
    db.session.commit()
    return 'Permission Denied'
