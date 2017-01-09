# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 15:07:46 2016

@author: xfhelen
# 获取对象信息
"""
class Person(object):
    def __init__(self, pID):
        self.__pID = pID
    def run(self):
        print 'I am a person'

class Man(Person):
    def __init__(self, pID, sex):
        self.__pID = pID
        self.__sex = sex
    def run(self):
        print 'I am a man'

# 判断对象类型 - type()
man = Man(511, 'M')
print type(123)
print type('bob')
print type(man)

# isinstance (变量,类型)
print isinstance(man, Man)                                                                                      
# dir 获得一个对象的所有属性和方法
print dir(man)
