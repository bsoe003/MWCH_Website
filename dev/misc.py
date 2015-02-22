"""
Filename: loader.py
Author: Brian Soe
Description: Loads constant data from data directory.
Prerequisite: Flask server must be running.
"""
import zlib

path = 'dev/data/'

def load(filename):
    dataList =[]
    with open(path+filename) as f:
        lines = f.readlines()
        f.close()
    header = lines[0].strip().split(',')
    for i in range(1,len(lines)):
        info = lines[i].strip().split(',')
        datum = dict(zip(header,info))
        dataList.append(datum)
    return dataList

def encrypt(phrases):
    return zlib.compress(phrases)

def decrypt(phrases):
    return zlib.decompress(phrases)