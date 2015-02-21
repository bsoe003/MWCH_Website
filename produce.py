"""
Filename: produce.py
Author: Brian Soe
Description: Produces rendered pages to static files.
Prerequisite: Flask server must be running.
"""

from bs4 import BeautifulSoup
import urllib2
import subprocess
import sys
import os
import re

orig_prettify = BeautifulSoup.prettify
r = re.compile(r'^(\s*)', re.MULTILINE)

routes = ['',
    'about/background', 'about/muiristas', 'about/sources',
    'menu/regular', 'menu/blended_iced', 'menu/pastries',
    'stories',
    'gallery']
root = 'production/'
static = 'dev/static/'

def prettify(self, encoding=None, formatter="minimal", indent_width=4):
    return r.sub(r'\1' * indent_width,
        orig_prettify(self, encoding, formatter))

def clean():
    for files in os.listdir('.'):
        if '.zip' in files:
            subprocess.call(['rm','-rf',files])
    for directory in os.listdir(root):
        subprocess.call(['rm','-rf',root+directory]) 

def file_transfer():
    for directory in os.listdir(static):
        subprocess.call(['cp','-r',static+directory,root])

def route_transfer(host,route):
    path = root+'pages/'
    text = urllib2.urlopen(host+route).read()
    soup = BeautifulSoup(text).prettify()
    filename = path+'index.html' if not route else path+route+'.html'
    try:
        html = open(filename,'w')
    except:
    	newpath = filename.split('/')
        os.makedirs('/'.join(newpath[:-1]))
        html = open(filename,'w')
    html.write(unicode(soup).encode('iso-8859-1'))
    html.close()

def zip_files(name='protoype'):
    filename = 'Group2_NoSLP_%s.zip' % name
    for files in os.listdir('.'):
        if '.zip' in files:
            subprocess.call(['rm','-rf',files])
    os.chdir(root)
    for directory in os.listdir('.'):
        subprocess.call(['zip','-r',filename, directory])
    subprocess.call(['mv',filename,'..'])

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'clean':
        prompt = '\033[93m[WARNING]\033[0m This will delete all production files. Are you sure? '
        answer = raw_input(prompt).lower().strip()
        if not answer or answer == 'yes' or answer == 'y':
            clean()
            print 'All production files removed successfully'
        exit(0)

    host = 'http://localhost:5000/'
    try:
        urllib2.urlopen(host)
    except:
        print '\033[91m[ERROR]\033[0m No localhost found. Please run: "python server.py"'
        exit(1)

    sys.stdout.write('Transferring from dev to production ... ')
    file_transfer()
    sys.stdout.write('\033[92mDONE\033[0m\n')
    sys.stdout.write('Transferring from routes to production ... ')
    BeautifulSoup.prettify = prettify
    for route in routes:
        route_transfer(host,route)
    sys.stdout.write('\033[92mDONE\033[0m\n')

    if len(sys.argv) > 1 and sys.argv[1] == 'zip':
        print 'Zipping production files ... '
        try:
            zip_files(sys.argv[2])
        except:
            zip_files()
        print '\033[92mDONE\033[0m'
    