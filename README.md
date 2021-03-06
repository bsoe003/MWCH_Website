# NoSLP [COGS 187B]
Website: Muir Woods Coffee House

### Preparation (Tentative)
This website needs following essential tools:
* Flask 0.10.1
* SQLAlchemy 0.9.7
* Flask-Mail 0.9.1
* Beautiful Soup 4.3.2
* Sass 3.4.13

These tools can installed through **pip**, a Python package installer. The execution of these files MUST be done through Python 2.7.x. This will not work with Python 3+. The download link for Python is located under "Helpful links".

You may obtain pip installer through:
> https://bootstrap.pypa.io/get-pip.py

*Note:* Python 2.7.9 has built-in pip installer, so downloading may not be necessary.

To install Sass, you may need to install **Gem** (Ruby package installer). Different operating systems have different ways of installing Gem, but make sure it works in command line/terminal.

```
[sudo] python get-pip.py
[sudo] bash setup.sh
```
Helpful links:
> https://www.python.org/downloads/

> https://pip.pypa.io/en/latest/installing.html

> https://www.ruby-lang.org/en/downloads/

> https://rubygems.org/pages/download


### Server (Tentative)
A part of this website needs server in order to submit a form. The server must be activated in order to view HTML files under "**dev**" directory.
```
python server.py
```
To kill the server, simply press "**ctrl**+**c**"

### Routes (Tentative)
The following are available routes for this website:
```
/
/about
/menu
/gallery
/stories
```

Each of these routes have its HTML file equivalence named and structured in same way (with exception '/' which is 'index.html').

### File Structure (Tentative)
There are 4 essential structures for this website. Each has its unique responsibility, so be sure to understand them.
#### root
All the files exist in the root directory are for administration. This includes activating sever, producing static files, list of dependencies, etc.
#### dev
This directory should contain files that meant for designing (both in UI and DB sense). It also holds "routes.py" which maps the route name to its corresponding html files.
#### production
This is a directory that holds all static file generated by "produce.py" (see "Production" section below). It helps to see what grader will see as an end result.
#### test
TBA

### Jinja2 Templating
All HTML files will contain some type of Jinja2 syntax to help bring back-end data to the display. It is an embedded schema where coders can write controllable logic such as conditional statement, iterative statement, calling variables, etc. It also helps reduce tedious repetition of HTML with its "extends" feature; one can create a template page where more detailed HTML files can use this template to reduce the amount of code written and time.

For more information: http://jinja.pocoo.org/docs/dev/

### base.html and static

All CSS and JavaScript files shoud go under static folder or else it will not work. All general linking process of CSS and JS should be done in base.html. Only exception to this is if certain CSS or JS is applicable certain page only! The convention is easy and simple. For link, script, img, a tag, their href or src should start with '/'. For example:

```html
<link rel="stylesheet" href="/[path]" />
```
More tags require href or src will be updated.


### Database
For the purposes of this development, the database will be handled by a Flask extension called "Flask-SQLAlchemy." This extension helps with modeling database with Python as well as calling data from it. The database itself will not be saved through repository; hence, creating and migrating database is necessary.

To activate database:
```
cd database
python _create.py
python _migrate.py
```

To destroy database for resetting purposes:
```
python _clean.py
```

[Heroku Instruction TBA]

### Emails
Sample email being used for this website will be "mwch.test001@gmail.com" (this will be the message sender). Everytime the user submits a story, this email will send it to individuals who need to approve the story. This is done through another Flask extension called "Flask-Mail"

TODO: UI for approving messages

### Production
COGS 187B grader should neither run server locally nor install dependencies. A script called "**produce.py**" can generate static files along with their dependent CSS and JavaScript **files while running the server**. To generate such files:
```
python produce.py
```
If there is a fault in "**production**" directory, you may clean "**production**" by:
```
python produce.py clean
```
To create a zip file for turn-in:
```
python produce.py zip [assignment_name]
```
