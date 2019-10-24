from heapq import *
class solution:
    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.total_n = 0


    def median_of_flow(self,ch):
        if self.total_n == 0:
            self.minheap.append(ch)
            self.total_n+=1
            return ch
        if self.total_n&1==1:
            heappush(self.maxheap,-ch)
            self.total_n+=1
            if -self.maxheap[0] > self.minheap[0]:
                self.maxheap[0], self.minheap[0] = -self.minheap[0], -self.maxheap[0]
                heapify(self.minheap)
            return (self.minheap[0] - self.maxheap[0]) / 2
        else:
            heappush(self.minheap,ch)
            self.total_n += 1
            if -self.maxheap[0]>self.minheap[0]:
                self.maxheap[0], self.minheap[0] = -self.minheap[0],-self.maxheap[0]
                heapify(self.maxheap)
            if len(self.minheap)>len(self.maxheap):
                return self.minheap[0]
            else:
                return -self.maxheap[0]



if __name__ == '__main__':
    so = solution()
    print(so.median_of_flow(4))
    print(so.median_of_flow(1))
    print(so.median_of_flow(3))
    print(so.median_of_flow(9))
    print(so.median_of_flow(12))
    print(so.median_of_flow(3))
    print(so.median_of_flow(8))
    print(so.median_of_flow(0))
    print(so.median_of_flow(-1))
    print(so.median_of_flow(4))
    print(so.median_of_flow(4))
    print(so.median_of_flow(4))
    print(so.median_of_flow(4))
    print(so.median_of_flow(4))
    print(so.median_of_flow(4))
    print(so.median_of_flow(4))
    print(so.median_of_flow(4))
    print(so.median_of_flow(4))
