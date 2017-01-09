# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:21:24 2016

@author: xfhelen
出错，测试是和调试
http://www.runoob.com/python/python-exceptions.html

"""

# try ... except ... except.... finaly

def evaluate(score):
    if score > 90:
        print 'Excellent'
    elif score > 80:
        print 'Good'
    elif score > 60:
        print 'OK'
    else:
        print 'Bad'
        
# 调试
# print - 但是之后删除print比较麻烦
# 断言 - assert
def foo(s):
    n = int(s)
    # 当n==0时，是一个AssertionError
    #当n!=0时，直接往下执行
    assert n != 0, 'n is zero!'
    return 10 / n


if __name__ == '__main__':
    try:
        score = int(s = raw_input('Score:'))
    except BaseException:
        print 'Not a number'
    finally:
        print 'Exit'

    foo(0)
# python -0 .py - 关闭assert



