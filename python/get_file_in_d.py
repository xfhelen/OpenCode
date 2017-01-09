# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 21:30:12 2017

@author: xfhelen
#### Get all the file in a directory
"""
import os

def getFileList(directory):
        directory = directory
        if directory == "":
            print 'no Sub-file!'
            return [ ]
        directory = directory.replace( "/","\\")
        if directory[-1] != "\\":
             directory = directory + "\\"
        a = os.listdir(directory)
        # print 'a = ', a
        # print 'hahahaha'
        path = [x   for x in a if os.path.isfile(directory + x)]
        return path
        
if __name__ == '__main__':
    directory = os.getcwd()
    print 'directory = ', directory
    path = getFileList(directory)
    print path
        