# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 19:37:14 2016

@author: xfhelen
# 示例代码 - http://github.com/pydata/pydata_book
# ctrl+c 中断执行的程序
# ctrl+r 搜索
# ctrl+l 清屏

###调试###
# q - 退出调试器
# n - 执行下一条命令
# b
# b 行号 - 设置断点
# c - 恢复执行

# ipython notebooks
"""


##########Numpy##################
# 常用模块的命名惯例
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
narr1 = np.array(data)
print narr1, narr1.ndim, narr1.shape
# 定义全一/零数组
narr2 = np.ones((3, 4))
narr3 = np.zeros(8)
narr4 = np.arange(8)
print 'narr2 = ', narr2, 'narr3 = ', narr3

# 矢量化 - 大小相等的数组的任意运算都会运用到元素级
arrA = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print 'arrA*arrA = ', arrA*arrA
print 'arrA+arrA = ', arrA+arrA
print 'arrA-arrA = ', arrA-arrA
print '1/arrA = ', 1/arrA
print 'arrA**0.5', arrA**0.5

# 转置
print arrA.T

# 通用函数 ufunc
print np.abs(arrA)
# 加一行 - axis表示维度
print' arrA = ', np.append(arrA, [[9, 10, 11]], axis=0)
# 加一列 - 2 = index
print np.insert(arrA, 2 , [9 , 10, 11], axis = 1)
print np.min(arrA), np.max(arrA)
# ** - 指数
print np.sqrt(arrA)
print arrA**0.5

# arange(up-thresold, low-thresold, interval)
points = np.arange(-5, 5, 0.01)
values = np.arange(0, 100, 0.1)
vs, ps = np.meshgrid(points, values)
z = np.sqrt(vs**2 + ps**2)
print 'vs = ', vs
print 'ps = ', ps
print 'z = ', z

# np.where(condition, x, y) - x if condition else y
xarr = np.arange(0 , 10 , 1)
yarr = np.arange(-10, 0 , 1)
condition = [True, False, False, False, True, False, True, True, False, True]
print np.where(condition, xarr, yarr)
print 'abs', np.where(yarr < 0 , np.abs(yarr), yarr)

print np.arange(1, 5, 1)
numArr = np.array([[4, 5, 6], [12, 24, 12]])
print np.array(numArr)
print numArr.mean()
# 统计行/列上的平均数/和
print numArr.mean(axis=0)
print numArr.sum(axis=1)
arrB = random.randint(5 , 3)
print arrB
# print np.unique(numArr)

print 'random.randint(5 , 8)'