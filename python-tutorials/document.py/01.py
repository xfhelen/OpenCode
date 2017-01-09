# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:56:42 2016

@author: xfhelen

List and tuple的使用方法
"""

# 内置数据类型 - 列表 - list - []
person1 = ['man', 20, 1.75, 'Bob']
for i in person1:
        print i
#倒数第一个数：Bob
print person1[-1], person1[-2], len(person1)
sex1 = ['sex:', 'man']
# modify
person1[0] = sex1
hometown1 = ['hometown:', 'Sichuan']
# append
person1.append(hometown1)
bio1 = ['bio:', 'master']
# insert
person1.insert(1, bio1)
print person1
print person1[1][1]
print person1.count(hometown1)
# count 统计有几个value
p = [1,1]
print p.count(1)

# tuple - 元组 - 一旦初始化便不能修改 - ()
#空tuple
tuple1 = ()
print tuple1
# 初始化之后便不可修改
tuple1=(1,2,3)
print tuple1
#一个元素的tuple必须按照以下格式，否则()会被当做一般()
tuple2=(1,)
notTuple2 = (1)
print tuple2, notTuple2






