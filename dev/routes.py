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
    return render_template('index.html')

@app.route('/about')
def viewAbout():
    """ Renders About page """
    muirisitas = loader.load('about_muiristas.tsv') # load gallery image data
    sources = loader.load('about_sources.tsv') # load gallery image data
    return render_template('about.html')

@app.route('/menu')
def viewMenu():
    """ Renders Menu page """
    return render_template('menu.html')

@app.route('/stories', methods=['GET','POST'])
def viewStories():
    Stories = models.Stories
    if request.method == 'POST':
        text = request.form['q']
        story = Stories(date=datetime.now(),text=text,approval=True)
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
        stories=stories)

@app.route('/gallery')
def viewGallery():
    """ Renders Gallery page """
    gallery = loader.load('gallery_photos.tsv') # load gallery image data
    return render_template('gallery.html',
        gallery=gallery)

@app.route('/sample')
def viewSample():
    """ Renders sample page for reference. DELETED SOON """
    return render_template('sample.html')
