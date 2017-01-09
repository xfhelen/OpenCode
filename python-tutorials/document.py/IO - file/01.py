# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 19:51:03 2016

@author: xfhelen
excel 操作
"""
import xlrd
f = xlrd.open_workbook('attack.csv')
for line in f:
    print line

