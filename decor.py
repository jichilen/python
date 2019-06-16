# coding=utf-8
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
            print ('begin call %s:' % func.__name__)
            func(*args, **kw)
            print( 'end call %s:' % func.__name__)

        return wrapper()

    return decorator


@log('execute')
def now():
    print ('2013-12-25')

#实现与上面相同的功能
#实现with+类需要修改__enter__以及__exit__属性
def with_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        with _ConnectionCtx():
            return func(*args, **kw)

    return wrapper()


class _ConnectionCtx():
    def __enter__(self):
        print('begin call ')

    def __exit__(self, exctype, excvalue, traceback):
        print ('end call ')


@with_connection
def rnow():
    print ('2014-12-25')


if __name__ == '__main__':
    print ('1')