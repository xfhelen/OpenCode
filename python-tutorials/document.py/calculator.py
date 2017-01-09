# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:33:38 2016

@author: xfhelen
# 
"""
import numpy as np
import pandas as pd

def cal(data):
    data_sum = sum(data)
    data_s_sum = sum(data**2)
    data_sum_s = sum(data)**2
    return data_sum, data_sum_s, data_s_sum
    
    
if __name__ == '__main__':
    a = np.array([21.9,21.7,21.8,21.4])
    print cal(a)



