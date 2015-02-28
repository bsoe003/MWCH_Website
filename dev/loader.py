"""
Filename: loader.py
Author: Brian Soe
Description: Loads constant data from data directory.
Prerequisite: Flask server must be running.
"""

path = 'dev/data/'

def load(filename):
    """ Load tsv files and convert to a list of dictionary """
    dataList =[]
    with open(path+filename) as f:
        lines = f.readlines()
        f.close()
    header = lines[0].strip().split('\t') # assume all keys are in first line
    for i in range(1,len(lines)):
        info = lines[i].strip().split('\t')
        datum = dict(zip(header,info)) # dictionary conversion
        dataList.append(datum)
    return dataList
