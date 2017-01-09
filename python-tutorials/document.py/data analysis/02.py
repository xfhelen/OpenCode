# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 19:52:23 2016

@author: xfhelen
"""

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

data1 = pd.read_csv('data.csv')
data1.columns = [1, 2, 3, 4]
data3 = data1.abs()
print data3
print data1, data1**0.5, data1+100
data2 = DataFrame([])
for column in data1:
    print column
    data2[column] = data1[column].tolist()[:500]

print data2

data2.to_excel('result.xlsx', sheet_name = 'Sheet2')

print 'OVER'




#
#
#
#
#data = Series(np.random.randn(10),
#              index = [['a', 'a', 'a', 'b' ,'b', 'b', 'c', 'c', 'd', 'd'] , [1,2,3,1,2,3,1,2,2,3]])
#print data
#print data.unstack()
#
#data = pd.read_csv('data.csv')['battFast_adap']
#print data
#
#chunker = pd.read_csv('data.csv', chunksize = 5000)
#tot = Series([])
#for peice in chunker:
#    tot = tot.add(peice['battFast_adap'].value_counts(), fill_value=0)
#tot = tot.order(ascending = False)
#
#print 'tot=',tot
#
#data.to_csv('result.csv')
