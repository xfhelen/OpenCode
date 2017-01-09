# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:06:06 2016

@author: xfhelen
"""

# 所有的数据类型都是对象
# 定义对象 - class 类名(继承类)
# 如果没有合适的继承类，就继承object类，这是所有对象最终都要继承的
class Student(object):
    # __init__(self, property1,...,propertyn)
    # __init__, self表示创建的实力本身, 所有的属性(包括数据和函数必须绑定到self，即采用self.)
    # 创建实例必须穿入对应property的参数
    # __init__定义必须绑定的参数
    def __init__(self, name, stID, score):
        # private属性 - __变量名
        self.__name = name
        self.__stID = stID
        self.__score = score
        # 除了传入的参数，还可以自己定义其他的属性
        self.sex = 'F'
    # private 函数
    def __getScore(self):
        if self.score > 98:
            print 'Excellent!'
        elif self.score > 60:
            print 'Good!'
        else:
            print 'Bad!'

# 创建类的实例 - 类名()
std1 = Student('Bob', '201192460', 98)
# 可以自由的给一个实例变量绑定一个属性 - 但是感觉这是不好的习惯
std1.__getScore()

