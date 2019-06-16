# coding=utf-8
'''
使用logging来代替print进行错误检查
可以通过level来调节显示
另外pdb可以是python 程序单步调试
'''
import logging

# DEBUG INFO WARNING ERROR
logging.basicConfig(level = logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
# print 10 / ns
