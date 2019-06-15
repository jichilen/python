'''
实现单例模式其实没有必要，python的module自带单例

如果一定要实现单例，有两种常见的做法
一种是使用装饰器
一种是使用__new__()
'''
import threading

def deco(cls):
    __instance={}
    def singlet(*args,**kwargs):
        if cls not in __instance:
            __instance[cls] = cls(*args,**kwargs)
        return __instance[cls]
    return singlet


@deco
class A:
    def __init__(self,x):
        self.x = x


class B:
    lock = threading.Lock()
    __instance={}
    def __init__(self, x):
        self.x = x
    def __new__(cls, *args, **kwargs):
        if cls not in B.__instance:
            with B.lock:
                if cls not in B.__instance:
                    B.__instance[cls] = object.__new__(cls)
        return B.__instance[cls]



if __name__ == '__main__':
    a1 = A(1)
    a2 = A(2)
    print(id(a1))
    print(id(a2))
    b1 = B(1)
    b2 = B(2)
    print(id(b1))
    print(id(b2))
