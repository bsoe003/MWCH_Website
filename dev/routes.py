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
import zlib

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
    muiristas = loader.load('about_muiristas.tsv')  # load gallery image data
    sources = loader.load('about_sources.tsv')  # load gallery image data
    return render_template('about.html',
                           endpoint="about",
                           muiristas=muiristas,
                           sources=sources)

@app.route('/menu')
def viewMenu():
    """ Renders Menu page """
    return render_template('menu.html', endpoint="menu")

@app.route('/stories', methods=['GET', 'POST'])
def viewStories():
    Stories = models.Stories
    if request.method == 'POST':
        text = request.form['q']
        date = datetime.now().strftime('%m/%d/%Y')
        story = Stories(date=datetime.now(), text=text, approval=True)
        db.session.add(story)
        db.session.commit()
        print "Saved to Database"
        #msg = Message("Hi 187B Graders",
        #    sender="NoSLP",
        #    recipients=["kirsh@ucsd.edu", "2flcastro@gmail.com", "adam@powe.rs", "huang.katie94@gmail.com"],
        #    cc=["brian.soe003@gmail.com", "dhyee@ucsd.edu", "cvd001@ucsd.edu"])
        #msg.html = 'We can tell that you are grading our project right now! Thank you for all your hard work, and have a great spring break!'
        #mail.send(msg)
        flash(u'Your story has been submitted.', 'success')
        return redirect('/stories')
    stories = Stories.query.filter(Stories.approval) \
        .order_by('date desc').all()
    return render_template('stories.html',
                           endpoint="stories",
                           stories=stories)

@app.route('/gallery')
def viewGallery():
    """ Renders Gallery page """
    photos = loader.load('gallery_photos.tsv')  # load gallery image data
    return render_template('gallery.html',
                           endpoint="gallery",
                           photos=photos)

@app.route('/approve')
def approveStory():
    stories = models.Stories.query.all()
    for story in stories:
        if story.id == int(request.form['id']):
            print story.approval
            story.approval = True
    db.session.commit()
    pass
