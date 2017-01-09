# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:25:14 2016

@author: xfhelen
装饰器 - decorator - 在代码运行期间动态增加功能
"""
# 函数也是对象，他有一个属性—_name_


# 在函数调用前自动打印日志
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
# 借助@作用，把decorator至于函数定义处，因此会把定义函数作为输入参数，并返回一个函数值
def now():
     print '2013-12-25'
print now.__name__

# 先执行log函数，在执行wrapper函数，log在wrapper内部执行
# 即便log与上述log同名也不会出现语法错误，相当于是一种函数继承
@log
def now():
     print '2013-12-25'
     
now()

# 可以发现：由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
print now.__name__
