# -*- coding: utf-8 -*-
# 让它按UTF-8编码读取
"""
Spyder Editor

This is a temporary script file.
"""

# name = raw_input('Your name:')
print 'Hello!'
print 1.2e6, -108, 0xff1, 400e-2

print "I'm OK"
print 'I\'m \"OK\"'
# r''表示内部的字符串默认不转义，\表示转义
print r'I am OK\\\\'
#'''表示多行内容'''
print '''line1
        line2
        line3'''
        
# r+'''    '''
print r'''line1
\line2'''

# bool 
print True, False
print 3 < 2
# 运算 and , or , not
print True and True, True and False, False and False
print True or True, True or False, False or False
print not True, not False

# 用大写的变量名表示常量
PI = 3.1413
print PI

# 整数除法永远是整数，想得到精确结果只需要*1.0
print 10/3, 10*1.0/3, 10/3*1.0, 10/(3*1.0)

# 格式化输出 %     %s, %nd, %.nf, %x， 转义%%
a = 3
b = 'plus'
print '%2d-%02d' % (3, 1)
print '%2d%%, %s, %.2f' % (a, b, PI)









