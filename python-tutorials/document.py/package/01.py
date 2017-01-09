# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 21:07:58 2016

@author: xfhelen
第三方库 - pypi.python.org
"""
# 在Python中，安装第三方模块，是通过setuptools这个工具完成的
# Python有两个封装了setuptools的包管理工具：easy_install和pip。目前官方推荐使用pip
# 通过在cmd下输入conda install ...安装第三方库
# Python提供了__future__模块，把下一个新版本的特性导入到当前版本，于是我们就可以在当前版本中测试一些新版本的特性

# 引入第三方库下的模块
import PIL.Image
import os
import calendar
import time
import datetime
import urllib

print os.O_RANDOM
print time.localtime()
print calendar.calendar(2015)
print datetime.date.year

im = PIL.Image.open('test.jpg')
print im.format
urllib.urlopen('http://www.baidu.com')

# 常用第三方库
# 科学计算 - numpy
# 图像 - PIL
#  os - 模块提供了访问操作系统服务的功能
# calendar - 时间 - time/datetime/
# urllib - 读取来自网上的数据
# https://www.zhihu.com/question/24590883
# http://wiki.jikexueyuan.com/project/start-learning-python/228.html

