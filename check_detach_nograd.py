import torch
from torch import nn

class A(nn.Module):
    def __init__(self):
        super(A, self).__init__()
        W=torch.tensor([1.,1],requires_grad=True)
        self.register_parameter('W',torch.nn.Parameter(W))
    def forward(self, x):
        x=self.W*x
        return x

class B(nn.Module):
    def __init__(self):
        super(B, self).__init__()
        W=torch.tensor([2.,2],requires_grad=True)
        self.register_parameter('W', torch.nn.Parameter(W))

    def forward(self, x):
        x = self.W * x
        return x

class C(nn.Module):
    def __init__(self):
        super(C, self).__init__()
        self.A=A()
        self.B=B()
        self.B.eval()
        for k in [self.B]:
            for param in k.parameters():
                print(param)
                param.requires_grad=False
    def forward(self, x):
        x=self.A(x)
        x=self.B(x)
        return x

if __name__ == '__main__':
    c=torch.tensor([2,2.])
    net=C()
    d=net(c)
    f=d.sum()
    optimizer = torch.optim.SGD(net.parameters(), 0.02, momentum=0.9)
    optimizer.zero_grad()
    f.backward(retain_graph=True)
    optimizer.step()