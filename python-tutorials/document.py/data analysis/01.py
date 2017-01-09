# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:32:34 2016

@author: xfhelen
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
# pandas
"""
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

set1 = [1, 2, 3, 4]
tuple1 = (5, 6, 7, 8)
s1 = Series(set1)
index1 = ['a', 'b', 'c', 'd']
s2 = Series(tuple1, index = index1)
print s1, s2

print s2['a']

#######pandas############
city = ['Beijing', 'Shanghai', 'Shenzhen', 'Xiamen']
population = [1234, 3452, 1256, 784]
debt = [234, 567, 789, 234]
dict1 = {'City':city, 'Population':population, 'Debt':debt}
frame1 = DataFrame(dict1)
print frame1
# 通过列索引
print frame1['City']
# 通过行索引
print frame1.ix[2]
frame2 = DataFrame(dict1, index=['A', 'B', 'C', 'D'])
print frame2
frame3 = frame2.append(frame1)
print frame3
year = ['2005', '2010', '2015']
frame4 = DataFrame(dict1, index=year)
