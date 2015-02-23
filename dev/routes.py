"""
Filename: routes.py
Author: Brian Soe
Description: List and defines all functionality of routes.
Prerequisite: Flask server must be running.
"""

from flask import *
from flask.ext.mail import Message
from datetime import datetime
from dev import app, db, models, loader, mail

@app.route('/')
def viewIndex():
    """ Renders homepage """
    return render_template('index.html', level=0)

@app.route('/about')
def viewAbout():
    """ When user goes to this route, redirect to available one """
    return redirect('/about/background')

@app.route('/about/background')
def viewBackground():
    """ Renders Background & History page """
    return render_template('about/background.html', level=1)

@app.route('/about/muiristas')
def viewMuiristas():
    """ Renders Muiristas page """
    data = loader.load('about_muiristas.csv') # load Muiristas data
    return render_template('about/muiristas.html', 
        level=1,
        muiristas=data)

@app.route('/about/sources')
def viewSources():
    """ Renders Where We Source From page """
    return render_template('about/sources.html', level=1)

@app.route('/menu')
def viewMenu():
    """ When user goes to this route, redirect to available one """
    return redirect('/menu/regular')

@app.route('/menu/regular')
def viewRegular():
    """ Renders Regular Drinks page """
    data = loader.load('menu_regular.csv') # load regular drinks data
    return render_template('menu/regular.html', 
        level=1,
        menu=data)

@app.route('/menu/blended_iced')
def viewBlended():
    """ Renders Blended & Iced Drinks page"""
    data = loader.load('menu_blended.csv') # load blended drinks data
    return render_template('menu/blended.html', 
        level=1,
        menu=data)

@app.route('/menu/pastries')
def viewPastries():
    """ Renders Pastries page """
    data = loader.load('menu_pastries.csv') # load pastries data
    return render_template('menu/pastries.html', 
        level=1,
        menu=data)

@app.route('/stories', methods=['GET','POST'])
def viewStories():
    Stories = models.Stories
    if request.method == 'POST':
        text = request.form['q']
        story = Stories(date=datetime.now(),text=text,approval=False)
        db.session.add(story)
        db.session.commit()
        #msg = Message("New story has been submitted",
        #    sender="mwch.test001@gmail.com", 
        #    recipients=["bsoe@ucsd.edu"])
        #msg.html = '<b>%s</b>' % text
        #mail.send(msg)
        flash("Your story has been submitted.")
        return redirect('/stories')
    stories = Stories.query.filter(Stories.approval) \
        .order_by('date desc').all()
    return render_template('stories.html',
        level=0,
        stories=stories)

@app.route('/gallery')
def viewGallery():
    """ Renders Gallery page """
    data = loader.load('gallery_photos.csv') # load gallery image data
    return render_template('gallery.html',
        level=0,
        gallery=data)

@app.route('/sample')
def viewSample():
    """ Renders sample page for reference. DELETED SOON """
    return render_template('sample.html', level=0)
