def printdec(func):
    def inerfun(*args, **kwargs):
        re = func(*args, **kwargs)
        print(func.__name__,args[0].queue, re)
        return re

    return inerfun


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0 for _ in range(k)]
        self.len = k
        self.begin = -1
        self.end = -1

    @printdec
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.end = 0
            self.begin = 0
            self.queue[0] = value
        else:
            self.begin += 1
            if self.begin>= self.len:
                self.begin = 0
            self.queue[self.begin] = value
        return True

    @printdec
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self.end == self.begin:
            self.end = -1
            self.begin = -1
            return True
        tmp = self.end + 1
        if tmp >= self.len:
            tmp = 0
        self.queue[self.end] = 0
        self.end = tmp

        return True

    @printdec
    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.end]

    @printdec
    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.begin]

    @printdec
    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.begin == -1:
            return True
        return False

    @printdec
    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.isEmpty():
            return False
        tmp = self.begin + 1
        if tmp >= self.len:
            tmp = 0
        if tmp == self.end:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

if __name__ == '__main__':
    que = MyCircularQueue(5)
    que.isEmpty()
    que.isFull()
    que.enQueue(1)
    que.deQueue()
    que.enQueue(2)
    que.enQueue(3)
    que.deQueue()
    que.Rear()
    que.Front()
    que.enQueue(3)
    que.enQueue(3)
    que.enQueue(3)
    que.isEmpty()
    que.isFull()
