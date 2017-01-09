# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:21:23 2016

@author: xfhelen
IO 编程 - 文件读写
文件夹操作
"""
# 返回一个list
import os

class Stuent():
    def __init__(self, name, sID):
        self.name = name
        self.sID = sID
        self.__score = 0
        self.__hometown = 'Beijing'
    def set_score(self, score):
        self.score = score

if __name__ == '__main__':
    # 打开文件
    f = open('data.txt', 'r')
    # 读完文件包括'\n'
    print 'readlines = ', f.readlines()
    # 回到文件头
    f.seek(0)
    # 一次性读取文件 
    print 'read = ', f.read()
    f.seek(0)
    print f.readline()
    # 文件指针位置 - byte
    print 'tell = ', f.tell()
    print f.readline()
    print f.tell()
    for line in f:
        # 读行
        print 'readline = ', line
    # 关闭文件
    f.close()
    
    # 按行读取文件
    f = open("data.txt")             # 返回一个文件对象
    line = f.readline()             # 调用文件的 readline()方法
    while line:
        print line,                 # 后面跟 ',' 将忽略换行符
        # print(line, end = '')　　　# 在 Python 3中使用
        line = f.readline()
        print line[2]
    f.close()
    os.rename('06.py', '00.py')
#    f = open('data.txt', 'w')
#    list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#    # f.write(str(list1))
#    f.write('Hello')
#    f.close()
#    f.open('data.txt', 'w')
#    f.seek = -0
#    f.write('world')
#    f.close()
    
    