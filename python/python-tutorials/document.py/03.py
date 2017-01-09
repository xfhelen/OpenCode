# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 16:42:32 2016

@author: xfhelen
dict and set
"""
# 字典 - {'key':value}
# 存放位置不能确定, 根据key hash
dict1 = {'bob':25,'bob':25,'bob':25, 'ada':37, 'helen':48}
for person in dict1:
    print person, dict1[person]
# get the value in key index
print dict1.get('bob', -1), dict1['bob']
print dict1.get('alice', -1)
# 判断key是否存在
# 1
if 'bob' in dict1:
    print dict1['bob']
else:
    print 'bob', 'No bob!'
# 2
if dict1.get('alice', -1) == -1:
    print 'No alice!'
else:
    print 'alice', dict1['alice']
# insert 
dict1['alice']=9
print dict1
# set - 集合 - set()
# set 和 dict 唯一的区别在于set只存key不存value，二者都没有重复的key值
set1 = set([4, 6, 7])
set2 = set([4, 6, 6, 8, 7])
print 'set1', set1, 'set2', set2
print len(set2)
# 交 &
print set1 & set2
# 并 |
print set1 | set2

# 可变对象 list VS 不可变对象 字符串， 不是指被复制了字符串的变量额
# 字符串
a = 'abc'
b = a.replace('a', 'A')
print 'a', a, 'b', b

# list 
a = ['c', 'b', 'a']
a.sort()
print a
