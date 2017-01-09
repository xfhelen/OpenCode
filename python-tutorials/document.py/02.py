# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 16:01:27 2016

@author: xfhelen
程序控制语句 - 选择 and 循环
"""
# 选择 - if-elif-else
age = raw_input('Your age:')
# 输入都是字符串,需用int转化成数字,如果输入不是数字字符串，则报错
age = int(age)
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'
    
# 循环 - for x in y  or  while
# for x in y 把y中每个元素带到x中,
tuple1 = ('Jason', 'man', 25, 1.78, 76)
for tuplei in tuple1:
    print tuplei
# range 生成0-value-1的整数序列
for i in range(10):
    print i
    
# while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum




