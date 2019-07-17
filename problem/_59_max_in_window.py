from collections import deque
def max_in_window(nums,k):
    maxv = deque()
    out = []
    for i in range(len(nums)):
        while len(maxv)>0 and maxv[0]<i-k+1:
            maxv.popleft()
        while len(maxv)>0 and nums[maxv[-1]]<=nums[i]:
            maxv.pop()
        maxv.append(i)
        if i >= k-1:
            out.append(nums[maxv[0]])
    return out

class queue_withmax():
    def __init__(self):
        self.que = deque()
        self.maxq = deque()
        self.k = 0
        self.ph = 0

    def push_back(self,a):
        self.que.append(a)
        self.k+=1
        while len(self.maxq) > 0 and self.que[self.maxq[-1]-self.ph-1] <= a:
            self.maxq.pop()
        self.maxq.append(self.k)

    def pop_front(self):
        self.que.popleft()
        self.ph+=1
        while len(self.maxq)>0 and self.maxq[0]<self.ph+1:
            self.maxq.popleft()

    def get_max(self):
        if len(self.maxq)==0:
            return None
        return self.que[self.maxq[0]-self.ph-1]

    # def update_p(self):
    #     if self.k>100:
    #         self.k=0
    #     if self.ph>100:
    #         self.ph=0


if __name__ == '__main__':
    print(max_in_window([2,3,4,2,6,2,5,1],3))
    qqq = queue_withmax()
    print(qqq.get_max())
    qqq.push_back(5)
    print(qqq.get_max())
    qqq.push_back(2)
    print(qqq.get_max())
    qqq.push_back(4)
    print(qqq.get_max())
    qqq.push_back(3)
    print(qqq.get_max())
    qqq.pop_front()
    print(qqq.get_max())
    qqq.pop_front()
    print(qqq.get_max())
    qqq.pop_front()
    print(qqq.get_max())
    qqq.pop_front()
    print(qqq.get_max())