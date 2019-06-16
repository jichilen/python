import torch
from torch import nn


class A(nn.Module):
    def __init__(self, a, b, f, **kwargs):
        super(A, self).__init__()
        self.a = a
        self.b = b
        self.f = f


class B(A):
    def __init__(self, a, b, c=1, d=1, **kwargs):
        super(B, self).__init__(a, b, **kwargs)
        self.c = c
        self.d = d
        assert self.f != None


class C(nn.Module):
    def __init__(self, a, b, h, **kwargs):
        super(C, self).__init__()
        self.B = B(a, b, **kwargs)
        self.h = h


if __name__ == '__main__':
    # 可以看到，在这个例子中，可以通过kwargs动态的将参数传递给类中对象的父类的初始化
    net = C(1, 2, 3, c=2, d=2, f='a')
    print(net)
