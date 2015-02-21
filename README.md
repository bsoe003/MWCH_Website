# NoSLP [COGS 187B]
Website: Muir Woods Coffee House

### Preparation (Tentative)
This website needs following essential tools:
* Flask 0.10.1
* SQLAlchemy 0.9.7
* Beautiful Soup 4.3.2

These tools can installed through **pip**, a Python package installer. The execution of these files MUST be done through Python 2.7.x. This will not work with Python 3+. The download link for Python is located under "Helpful links".

You may obtain pip installer through:
> https://bootstrap.pypa.io/get-pip.py

```
[sudo] python get-pip.py
[sudo] pip install -r requirements.txt
```
Helpful links:
> https://www.python.org/downloads/
> https://pip.pypa.io/en/latest/installing.html


### Server (Tentative)
A part of this website needs server in order to submit a form. The server must be activated in order to view HTML files under "**dev**" directory.
```
python server.py
```
To kill the server, simply press "**ctrl**+**c**"

### File Structure (TBA)

### Using Jinja2 Templating (TBA)

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
