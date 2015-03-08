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
    Stories = models.Stories
    stories = Stories.query.filter(Stories.approval) \
        .order_by('date desc').all()
    return render_template('index.html', 
        endpoint="home",
        stories=stories)

@app.route('/about')
def viewAbout():
    """ Renders About page """
    muiristas = loader.load('about_muiristas.tsv') # load gallery image data
    sources = loader.load('about_sources.tsv') # load gallery image data
    return render_template('about.html', 
        endpoint="about",
        muiristas=muiristas,
        sources=sources)

@app.route('/menu')
def viewMenu():
    """ Renders Menu page """
    return render_template('menu.html', endpoint="menu")

@app.route('/stories', methods=['GET','POST'])
def viewStories():
    Stories = models.Stories
    if request.method == 'POST':
        text = request.form['q']
        date = datetime.now().strftime('%m/%d/%Y')
        story = Stories(date=datetime.now(),text=text,approval=True)
        db.session.add(story)
        db.session.commit()
        print "Saved to Database"
        #msg = Message("New story has been submitted",
        #    sender="NoSLP", 
        #    recipients=["bsoe@ucsd.edu","dhyee@ucsd.edu","cvd001@ucsd.edu"])
        #msg.html = 'The following story needs an approval:<br/><br/>'\
        #    +'<b>Date:</b> '+date+'<br/><b>Story:</b> '+text+'<br/><br/>'
        #mail.send(msg)
        flash(u'Your story has been submitted.','success')
        return redirect('/stories')
    stories = Stories.query.filter(Stories.approval) \
        .order_by('date desc').all()
    return render_template('stories.html',
        endpoint="stories",
        stories=stories)

@app.route('/gallery')
def viewGallery():
    """ Renders Gallery page """
    photos = loader.load('gallery_photos.tsv') # load gallery image data
    return render_template('gallery.html',
        endpoint="gallery",
        photos=photos)

@app.route('/approve', methods=['POST'])
def approveStory():
    pass
