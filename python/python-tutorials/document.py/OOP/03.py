# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 15:58:07 2016

@author: xfhelen
__slots__
"""
from types import MethodType
class Animal(object):
    def __init__(self):
        pass
    def run(self):
        print 'Animal is running'
class Dog(Animal):
    def __init__(self):
        pass
    __slots__ = ('name', 'age')
    def run(self):
        print 'Dog is running'
        
# 创建一个clas实例后，可以给它动态绑定任意属性
dog = Dog()
dog.run()
animal = Animal()
animal.run()
dog.name = 'juliet'
print dog.name
dog.sex = 'M'
print dog.sex

# 也可以给一个类绑定任意属性和功能
def set_name(self, name):
     self.name = name
Animal.set_name = MethodType(set_name, None, Animal)
dog.set_name('Jack')
animal.set_name('bob')
print animal.name
print dog.name

dog.type = 'type'
print dog.type

 

