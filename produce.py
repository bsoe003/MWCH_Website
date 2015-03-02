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
import glob

orig_prettify = BeautifulSoup.prettify
r = re.compile(r'^(\s*)', re.MULTILINE)

# list of routes available for this website
routes = ['', 'about', 'menu', 'stories', 'gallery']

# directories being used
root = 'production/'
static = 'dev/static/'

def prettify(self, encoding=None, formatter="minimal", indent_width=4):
    """ Re-initializing BeautifulSoup's prettify to adjust indent width """
    return r.sub(r'\1' * indent_width,
        orig_prettify(self, encoding, formatter))

def clean():
    """ Delte all files under production directory as well as zip file """
    for files in os.listdir('.'): # deleting zip file
        if '.zip' in files:
            subprocess.call(['rm','-rf',files])
    for directory in os.listdir(root): # deleting files under production
        subprocess.call(['rm','-rf',root+directory]) 

def file_transfer():
    """ Copy all static files from dev to production """
    subprocess.call(['rm','-r','.sass-cache'])
    for directory in os.listdir(static):
        subprocess.call(['cp','-r',static+directory,root])
    subprocess.call(['rm','-r',root+'scss'])

def route_transfer(host,route):
    """ Save a certain route as static HTML file to production """
    path = root # default path
    text = urllib2.urlopen(host+route).read() # grab html codes from route

    # format html code and fix css/js/anchor for static file
    soup = BeautifulSoup(text).prettify()
    anchors = re.compile(r'<a href="/[a-zA-Z0-9/]*"') #/ at 9
    for anchor in anchors.findall(soup):
        if anchor[10:-1] not in routes:
            continue
        if anchor[10:-1] == '':
            soup = soup.replace(anchor,
                (anchor[:9]+anchor[10:-1]+'index.html"'))
        else:
            soup = soup.replace(anchor,
                (anchor[:9]+anchor[10:-1]+'.html"'))

    # for '/' route, save as 'index.html'
    filename = path+'index.html' if not route else path+route+'.html'
    try:
        html = open(filename,'w')
    except: # create directory if doesn't exist
    	newpath = filename.split('/')
        os.makedirs('/'.join(newpath[:-1]))
        html = open(filename,'w')
    html.write(unicode(soup).encode('utf-8')) # appropriate encode for saving
    html.close()

def zip_files(name='protoype'):
    """ Zip files under production for assignment turn-in """
    filename = 'Group2_NoSLP_%s.zip' % name
    for files in os.listdir('.'): # remove previous zip file to avoid conflict
        if '.zip' in files:
            subprocess.call(['rm','-rf',files])
    os.chdir(root) # go to production directory
    for directory in os.listdir('.'): # zip each files in production
        subprocess.call(['zip','-r',filename, directory])
    subprocess.call(['mv',filename,'..']) # move zip files to root

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'clean': # check and perform clean
        prompt = '\033[93m[WARNING]\033[0m This will delete all production' \
            +'files. Are you sure? (Y/n) '
        answer = raw_input(prompt).lower().strip()
        if not answer or answer == 'yes' or answer == 'y':
            clean()
            print 'All production files removed successfully'
        else:
            print 'Removal Cancelled'
        exit(0)

    # Check if server is running
    host = 'http://localhost:5000/'
    try:
        urllib2.urlopen(host)
    except:
        print '\033[91m[ERROR]\033[0m No localhost found. Please run: "python server.py"'
        exit(1)

    # Transfer all static files
    sys.stdout.write('Transferring from dev to production ... ')
    file_transfer()
    sys.stdout.write('\033[92mDONE\033[0m\n')

    # convert route to static html files
    sys.stdout.write('Transferring from routes to production ... ')
    BeautifulSoup.prettify = prettify # redefine prettify function
    for route in routes:
        route_transfer(host,route)
    sys.stdout.write('\033[92mDONE\033[0m\n')

    if len(sys.argv) > 1 and sys.argv[1] == 'zip': # check and perform zip
        print 'Zipping production files ... '
        try:
            zip_files(sys.argv[2])
        except:
            zip_files()
        print '\033[92mDONE\033[0m'
    