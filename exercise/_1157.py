from collections import defaultdict, Counter
import math
from typing import List

class MajorityChecker:

    def __init__(self, arr: List[int]):
        s = int(math.sqrt(len(arr) * 2))
        count = Counter(arr)
        dic = {}
        cal = 0
        for k, v in count.items():
            if v > s // 2:
                dic[k] = cal
                cal += 1
        ass = [[0] * len(arr) for _ in range(len(dic))]
        #优化，增加一列ass可以避免y==0的讨论
        for y in range(len(arr)):
            for j in range(len(dic)):
                if dic[arr[y]] == j:
                    if y > 0:
                        ass[j][y] = ass[j][y - 1] + 1
                    else:
                        ass[j][y] = 1
                else:
                    if y > 0:
                        ass[j][y] = ass[j][y - 1]
                    else:
                        ass[j][y] = 0
        self.dic = dic
        self.ass = ass
        self.s = s
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        if right - left < self.s:
            obj = Counter(self.arr[left:right + 1])
            for cur, count in obj.items():
                if count >= threshold:
                    return cur
            return -1
        else:
            l = len(self.dic)
            for i in range(l):
                if left == 0:
                    tmp = self.ass[i][right]
                else:
                    tmp = self.ass[i][right] - self.ass[i][left - 1]
                if tmp >= threshold:
                    for k, v in self.dic.items():
                        if v == i:
                            return k
            return -1
'''
分块做法，从来没有见过的思路
这个思路可以将一个大的搜索问题拆分成很多小的问题，主要思路如下：
如果暴力，那么一次查询复杂度O(s)，超时，s是区间长度，最大为n，区间长度越小暴力的代价越低，区间长度越长，待查项其实越少，为2n/s
取s = sqrt(2n)，运算复杂度为sqrt(2n)，预处理复杂度n+n*sqrt(2n)，总复杂度o((n+q)*sqrt(2n))

当然这个题还可以用线段树来做

'''
