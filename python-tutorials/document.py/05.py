# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:29:07 2016

@author: xfhelen
高级特征
"""
from collections import Iterable

# list or tuple 切片  list[n:m:r]，从索引n开始取到m-1，按照r的间距取数
# m n表示索引号，：表示所有索引号
list1 = range(101)
# 按照间隙2，取第11到20个数
print list1[10 : 20 : 2]
# 按照间隙5取数
print list1[: : 5]

# 迭代 - for in
# 因为dict存储顺序不确定，所以每次输出结果可能不同
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key, d[key]

for value in d.itervalues():
    print key, value

for item in d.iteritems():
    print item

# 判断一个对象是否是可迭代对象
print isinstance('abc', Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance(123, Iterable)
# 引用两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y

# 把list索引和值变成key-value元素对 - enumerate
for i, value in enumerate(['A', 'B', 'C']):
     print i, value

for i, value in enumerate(list1):
    print i, value