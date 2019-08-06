import torch
from torch import nn

class A(nn.Module):
    def __init__(self):
        super(A, self).__init__()
        W=torch.tensor([1.,1],requires_grad=True)
        self.register_parameter('W',torch.nn.Parameter(W))
    def forward(self, x):
        x=self.W[None,...]*x
        return x

class B(nn.Module):
    def __init__(self):
        super(B, self).__init__()
        W=torch.tensor([2.,2],requires_grad=True)
        # self.register_parameter('W', torch.nn.Parameter(W))
        self.W = torch.nn.Parameter(W)

    def forward(self, x):
        x = self.W[None,...] * x
        return x

class C(nn.Module):
    def __init__(self):
        super(C, self).__init__()
        self.A=A()
        self.B=B()
        self.norm = nn.BatchNorm1d(2)
        self.norm.eval()
        self.A.eval()
        self.B.eval()
        # for k in [self.B]:
        #     for param in k.parameters():
        #         print(param)
        #         param.requires_grad=False
    def forward(self, x):
        x=self.norm(self.A(x))
        x=self.B(x)
        return x

class Bicubic(torch.autograd.Function):
    def __init__(self):
        pass
    def forward(self):
        pass
    def backward(self):
        pass



if __name__ == '__main__':
    def bahook(moduel,input,output):
        print(input)
        print(output)
    c=torch.tensor([[1,2.],[2,2.]])
    net=C()
    handle = net.norm.register_backward_hook(bahook)
    for _ in range(2):
        d=net(c)
        f=d.sum()
        optimizer = torch.optim.SGD(net.parameters(), 0.02, momentum=0.9)
        optimizer.zero_grad()
        f.backward(retain_graph=True)
        print(net.A.W.grad)
        optimizer.step()
        ppp=1