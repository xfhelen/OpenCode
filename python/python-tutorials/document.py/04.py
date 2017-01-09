# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:16:08 2016

@author: xfhelen
函数
"""
import math

# 调用函数 - http://docs.python.org/2/library/functions.html#abs
# 常用 abs(), int(), str()等
# help (abs)
a = abs
print a(-10)

# 定义函数 - def funName(inputArgument):

def add(x, y):
    return x+y
    
print add(2, 3)

def swap(a, b):
    temp = a 
    a = b
    b = temp
    return

a = 10
b = 20
print a, b
swap(a, b)
# 交换两个数值
a,b = b,a
print a, b

# 空函数
def nop():
    pass

# 函数返回参数 - return (value1, ...., valuen)
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
# 用过各变量接受tuple
x, y = move(100, 100, 60, math.pi / 6)
# 函数返回值实际上是一个tuple
r = move(100, 100, 60, math.pi / 6)
print x, y
print r

# 默认参数
# 默认参数必须在变动参数后面,调用函数提供参数可以不给默认参数提供数值
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5)
print power(5, 3)

# 可以按顺序提供默认参数，也可以不安顺序
def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

enroll('Adam', 'M', city='Tianjin')
# 默认参数必须指向不变对象
# wrong example
def add_end1(L=[]):
    if L is None:
        L = []
    L.append('END1')
    return L
print add_end1()
print add_end1() # wrong!!

# right 
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END2')
    return L
print add_end2()
print add_end2()

# 可变参数
# 1 把参数作为一个list或者tuple传进去,不支持无参情况
def calc1(number):
    sum = 0
    for i in number:
        sum = sum + i * i
    return sum

print calc1([1, 2, 3, 4])
print calc1((1, 2, 3, 4))
# print calc1()

# 利用可变参数 * - ()，参数number自动把接收到的内容转换成tuple，支持无参情况
def calc2(*number):
    sum = 0
    for i in number:
        sum = sum + i * i
    return sum

print calc2(1, 2, 3, 4)
print calc2(1, 2, 3, 4)
print calc2()

# *允许把tuple，list当做可变参数传进去
num = [1, 2, 3, 4]
print calc2(*num)

# 关键字参数 ** - {} - 必填和选填选项
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)

# 混合参数
# 在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，
#但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
def func(*args, **kw):
    for arg in args:
        print arg
    print kw
args = [1, 2, 3]
func(*args, **kw)
