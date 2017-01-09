# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:55:26 2016

@author: xfhelen
列表生成式 - [生成元素 + for in]
"""
from collections import Iterable

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print [x * x for x in list1]
print [str(m) + n for m in list1 for n in list2]
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

# 判断是否是自字符
print isinstance(123, str)
