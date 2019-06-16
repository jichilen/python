# 常见的有两种方式
# 第一种是循环列表
# 第二种是两个栈转列表
def deco(fun):
    def inf(*args,**kwargs):
        cls = args[0]
        try:
            re=fun(*args,**kwargs)
            print(re)
        except:
            fun(*args,**kwargs)
        print(cls.s1)
        print(cls.s2)
        print()
    return inf


class Stack2que():
    def __init__(self):
        self.s1 = [] #
        self.s2 = []

    @deco
    def push(self,num):
        self.s1.append(num)

    @deco
    def pop(self):
        if len(self.s2)>0:
            return self.s2.pop()
        while len(self.s1)>0:
            self.s2.append(self.s1.pop())
        if len(self.s2)>0:
            return self.s2.pop()
        print("error")
        return None


if __name__ == '__main__':
    que = Stack2que()
    que.push(12)
    que.push(1)
    que.push(13)
    que.push(2)
    que.pop()
    que.pop()
    que.pop()
    que.pop()
    que.pop()
    que.push(2)
    que.push(12)
    que.pop()
    que.push(21)
    que.push(22)
    que.pop()
    que.pop()
