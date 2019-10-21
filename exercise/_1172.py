import bisect
class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nums = [[]]
        self.nofull = []

    def push(self, val: int) -> None:
        if len(self.nofull)==0:
            if len(self.nums[-1])>=self.cap:
                self.nums.append([val])
            else:
                self.nums[-1].append(val)
        else:
            self.nums[self.nofull[0]].append(val)
            if len(self.nums[self.nofull[0]])>=self.cap:
                self.nofull = self.nofull[1:]

    def pop(self) -> int:
        while len(self.nums) and len(self.nums[-1]) == 0:
            self.nums.pop()
        if len(self.nums)==0:
            return -1
        return self.nums[-1].pop()

    def popAtStack(self, index: int) -> int:
        if len(self.nums)<=index:
            return -1
        if len(self.nums[index])==0:
            return -1
        ind = bisect.bisect(self.nofull,index)
        if index<len(self.nums)-1 and (ind-1<0 or self.nofull[ind-1]!=index):
            bisect.insort(self.nofull,index)
        return self.nums[index].pop()


if __name__ == '__main__':
    A=["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack",
     "pop", "pop", "pop", "pop", "pop"]
    B=[[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]
    for f,v in zip(A,B):
        if f=='DinnerPlates':
            so = DinnerPlates(v[0])
        else:
            if len(v)>0:
                print(getattr(so,f)(v[0]))
            else:
                print(getattr(so, f)())



# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)