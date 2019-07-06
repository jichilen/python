class stack_with_min:
    def __init__(self):
        self.stack = []
        self.min = None
        self.minstack = []

    def __repr__(self):
        return self.stack.__repr__()

    def push(self,num):
        self.stack.append(num)
        if self.min is None or num<self.min:
            self.min = num
        self.minstack.append(self.min)

    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def mins(self):
        return self.minstack[-1]


if __name__ == '__main__':
    a = stack_with_min()
    a.push(1)
    a.push(2)
    print(a)
    print(a.mins())
    a.push(2)
    a.push(0)
    print(a.mins())
    a.pop()
    print(a.mins())
