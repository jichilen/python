#coding=utf-8
'''
使用装饰器
是程序运行时可读性更高
比如在函数调用前后自动打印日志
'''

import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print 'begin call %s:' % func.__name__
			func(*args, **kw)
			print 'end call %s:'% func.__name__
		return wrapper()
	return decorator
	
@log('execute')
def now():
    print '2013-12-25'