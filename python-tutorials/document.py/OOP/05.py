# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:24:15 2016

@author: xfhelen

有四个数字：1、2、3、4，输出组成互不相同且无重复数字的三位数的个数以及三位数
"""
def norepeatedTrip():
    num = (1, 2, 3, 4)
    tripNum = []
    count = 0
    for i in num:
        for j in num:
            for k in num:
                if (i != j) and (j != k) and (i != j):
                    tripNum.append(i * 100 + j * 10 + k)
                    count = count +1
    print count, '\n', tripNum

def salary(profit):
    if profit > 100:
        pass
    elif profit > 60:
        pass
    elif profit > 40:
        pass
    elif profit > 20:
        pass
    elif profit > 10:
        pass
    elif profit > 0:
        pass
    else:
        print 'Error'
def salary2(profit):
    proArray = (0, 10, 20, 40, 60, 100)
    salaryArray = (0.1, 0.075, 0.05, 0.03, 0.015, 0.01)
    j = len(proArray)
    print j
    for i in range(1, j):
        if profit > proArray[j-i]:
            return (profit-proArray[j - i])*salaryArray[j - i]


if __name__ == '__main__':
    norepeatedTrip()
    profit = int(raw_input('Profit:'))
    print salary2(profit), 'W'
    

