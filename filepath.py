# -*- coding: utf-8 -*-
# @Author: xiweibo
# @Date:   2018-08-22 11:43:59
# @Last Modified by:   xiweibo
# @Last Modified time: 2018-08-22 15:11:11
"""
Python中，获取当前执行主脚本的方法有两个: 
如果当前文件包含在sys.path里面，那么，__file__返回一个相对路径！
如果当前文件不包含在sys.path里面，那么__file__返回一个绝对路径！
sys.argv[0] 获取主执行文件路径的最佳方法，可能是一个相对路径，取一下abspath保险起见
__file__
"""
import os
import sys

# 搜索模块的路径集合 可以通过sys.path.append往搜索模块中添加路径
print sys.path
# 返回当前脚本的文件路径，含文件名
print os.path.abspath(__file__)
print sys.argv[0] 
# 返回文件名绝对路径的上层路径可以多次使用
print os.path.dirname(os.path.abspath(__file__))
# 将文件分割成(head, tail)形式 用到了os.sep
print os.path.split(os.path.dirname(__file__))
# os.sep是当前操作系统使用的路径分隔符
print os.sep
#  将文件路径进行拼接
print os.path.join("E:\\project", "filepathutils\\test.py")
# os.path.normpath将文件的格式规格化，windows系统将'\\'、'\'变为'/'
print os.path.normpath("C:\\Clarence\\.\\Test\\test.py") # C:\Clarence\Test\test.py

"""
测试结果:
['E:\\project\\filepathutils', 'C:\\Windows\\SYSTEM32\\python27.zip', 'D:\\python2InstallLocation\\DLLs', 'D:\\python2InstallLocation\\lib', 'D:\\python2InstallLocation\\lib\\plat-win', 'D:\\python2InstallLocation\\lib\\lib-tk', 'D:\\python2InstallLocation', 'D:\\python2InstallLocation\\lib\\site-packages']
E:\project\filepathutils\filepath.py
E:\project\filepathutils\filepath.py
E:\project\filepathutils
('E:\\project', 'filepathutils')
\
E:\project\filepathutils\test.py
C:\Clarence\Test\test.py
[Finished in 0.3s]
"""