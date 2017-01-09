# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 21:19:23 2017

@author: xfhelen
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os.path
output_path1 = '../OUTPUT/DATA/'
output_path2 = '../OUTPUT/FIGURE/CDF'

# cdf = p(X<x)
def CDF(data):
    data_size=len(data)
    # set - 唯一化并排序
    # uniquifying and sequencing the data
    data_set=sorted(set(data))
    bins=np.append(data_set, data_set[-1]+12)
    # 计算data中每个数出现的频数
    # calculating the appearance of each different elements in data_set
    counts, bin_edges = np.histogram(data, bins=bins, density=False)
    # 每个数出现的概率 = 用每个数出现的频数/总数
    # appearance probability 
    counts=counts.astype(float)/data_size
    # cdf = p(X<x) = 所有小于x出现之和
    # cumsum - calcumalate sum
    cdf = np.cumsum(counts)
    return bin_edges, cdf
    
    
    
if __name__ == '__main__':
    x_label = 'Power'
    y_label = 'CDF'
    data = pd.read_csv(output_path1+'mix-attack/f1-w40.csv')
    fig = plt.figure()
    # call CDF
    for col in data.columns[1:-1]:
        bin_edges, cdf = CDF(data[col])
        plt.plot(bin_edges[0: -1], cdf, label=col)
        
    plt.ylim((0,1))
    plt.ylabel(y_label)
    plt.xlim(300, 800)
    plt.yticks(np.arange(0,1.1,0.1))
    plt.grid(True)
    plt.grid('off')
    plt.legend(loc='lower right')
    plt.show()
    plt.savefig(output_path2+'.jpg')

