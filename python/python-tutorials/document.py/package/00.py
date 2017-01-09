# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:48:18 2016

@author: xfhelen
使用模块
"""
# 引入模块
try:
    # import ... as ...为cStringIO指定别名为StringIO
    # 可以避免大幅度修改代码
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO
    
import sys
def test():
    args = sys.argv
    # argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

# 类似_xxx和__xxx这样的函数或变量就是非公开的（private）
# 类似__xxx___是特殊变量，属于公开变量 - public
# 一般的定义方法都是公开变量
# _private_1,_private_2都不能被其他模块直接应用，只能通过greeting引用
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name
    
def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# 运行当前脚本, if判断结果是true,如果是其他模块导入当前脚本（模块）,则if判断结果为false
# 作用，其他脚本引用时避免不必要的执行
if __name__=='__main__':
    test()
