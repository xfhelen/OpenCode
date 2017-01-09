# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 16:28:31 2016

@author: xfhelen
# running this script will delete all the output files under the path '../OUTPUT'
# 删除一个目录下的所有文件，但是保留子目录
"""
import os

# 将一个目录下的子目录与子文件分开
def classify_dir(directory):
    sub_directory = []
    sub_files = []
    # 参数不是一个目录
    if not os.path.isdir:
        print 'Input Parameter Error'
        print 'diectory is not a directory'
        return sub_directory, sub_files
    else:
        temp_dir = os.listdir(directory)
        if not temp_dir:
            print 'directory is EMPTY'
        else:
            for i in temp_dir:
                temp = directory+i
                if os.path.isdir(temp):
                    sub_directory.append(temp+'/')
                if os.path.isfile(temp):
                    sub_files.append(temp)
        return sub_directory, sub_files

def delete(directory):
    print 'processing ', directory
    sub_directory, sub_files = classify_dir(directory)
    # 删除子文件
    if not sub_files:
        print 'No sub files'
    else:
        for i in sub_files:
            print 'deleting ', i
            os.remove(i)
        
    if not sub_directory:
        print 'No sub directory'
        return
    else:
        for i in sub_directory:
            delete(i)
            
if __name__ == '__main__':
    
    path = '../OUTPUT/'
    print 'BEGIN'
#    sub_irectory, sub_files = classify_dir(path)
#    print 'sub_directory = ', sub_irectory
#    print 'sub_files = ', sub_files
    delete(path)
    print 'OVER'
    
    


