# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:34:26 2016

@author: xfhelen
# 继承和多态
"""
# 父类 - 继承object
class Animal(object):
    def __init__(self):
        pass
    def run(self):
        print 'Animal is running!'
# 子类
# 可以继承父类的所有属性
# 可以覆盖或者拥有自身属性
class Dog(Animal):
    def __init__(self):
        pass
    # 子类覆盖了父类的run
    def run(self):
        print 'Dog is runing'

class Cat(Animal):
    def __init__(self):
        pass
    def run_cat(self):
        print 'Cat is running'
        
def run_twice(animal):
    animal.run()
    animal.run()
def run_once(dog):
    dog.run()
    dog.run()
        
if __name__ == '__main__':
    animal = Animal()
    dog = Dog()
    cat = Cat()
    animal.run()
    dog.run()
    # 子类继承了父类run,并且没有覆盖
    cat.run()
    # dog 是Animal 类
    print isinstance(dog, Animal)
    # 但是animal不是dog类
    print isinstance(animal, Dog)
    # 对象作为函数参数
    run_twice(dog)
    run_once(dog)

