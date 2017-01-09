# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:08:13 2016

@author: xfhelen
pandas - 是python中处理数据最强大的库

"""
from pandas import Series, DataFrame
import pandas as pd

# 数据结构 - Series and DataFrame
# Series 是一个一维类似的数据结构,感觉像是一个可以用户指定的dict， 包含索引(index)和数值(value)
s = Series([4, 5, 43, 12], index = ['a', 'b', 'c', 'd'])
print s
print 'index = ', s.index, 'value = ', s.values
print s*2
print s[s > 40]
# 判断某索引是否存在Series实例中
print 4 in s
print 'a' in s
# 判断每个索引出的value是否缺少
print s.isnull()
# 名字
s.name = 'population'
s.index.name = 'state'
print s

# DataFrame - 类似电子表格的数据结构 - 每一个都可以是不同数据类型
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame1 = DataFrame(data)
print frame1
# 按列读
print frame1['state']
frame1.columns.name = 'state'

# 读某一行的第几个数
print frame1['state'][3]
# wrong - print fram1[3]
# 按行读
print frame1.ix[3]
frame1.index.name = 'year'
print frame1.values


# 假设你设定了一个顺序,dataframe按照你的顺序放
frame2 = DataFrame(data, columns = ['year','state', 'pop'])
print frame2
# 如果你传递了一个列但是没赋值，则赋值维NaN
frame3 = DataFrame(data, columns = ['year', 'state', 'pop', 'debt'])
print frame3



