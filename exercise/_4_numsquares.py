from collections import deque
from queue import Queue

class Solution:
    def numSquares(self, n: int) -> int:
        # first we need a generater to gen squares
        sq = (i * i for i in range(1000))
        for i, square in enumerate(sq):
            if square > n:
                break
        sql = [j * j for j in range(i)]
        # begin search
        expanding = Queue()
        expanding.put((0,0))
        expanded = set()
        while not expanding.empty():
            tmp,cal = expanding.get()
            cal += 1
            if tmp in expanded:
                continue
            expanded.add(tmp)
            if tmp == n:
                return cal-1
            for sq in sql:
                tsq = tmp + sq
                if tsq in expanded:
                    continue
                expanding.put((tsq,cal))
        return -1
    def numSquares1(self, n: int) -> int:
        # first we need a generater to gen squares
        sq = (i * i for i in range(1000))
        for i, square in enumerate(sq):
            if square > n:
                break
        sql = [j * j for j in range(i)]
        # begin search
        expanding = deque()
        expanding.append((0,0))
        expanded = set()
        while len(expanding)!=0:
            tmp,cal = expanding.popleft()
            cal += 1
            if tmp in expanded:
                continue
            expanded.add(tmp)
            if tmp == n:
                return cal-1
            for sq in sql:
                tsq = tmp + sq
                expanding.append((tsq,cal))
        return -1
    def numSquares2(self,n):
        around = []
        for i in range(1, n + 1):
            if i ** 2 <= n:
                around.append(i ** 2)
            else:
                break;

        r = 0
        seen = set()  # 防止重复运算

        # ----------------BFS 开始----------------------
        # 初始化根节点
        q = Queue()
        q.put((0, r))

        # 进入队列循环
        while not q.empty():
            # 取出一个元素
            cur, step = q.get()
            step += 1

            # 放入周围元素
            for a in around:
                a += cur
                if a == n:
                    return step
                if a < n and (a, step) not in seen:
                    seen.add((a, step))
                    q.put((a, step))
        # ----------------------------------------------
        return 0



if __name__ == '__main__':
    so = Solution()
    n = 380
    re = so.numSquares(n)
    n = 380
    re = so.numSquares1(n)
    re = so.numSquares2(n)
    print(re)
