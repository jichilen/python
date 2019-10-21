from typing import List
from collections import defaultdict


class node(object):
    def __init__(self):
        self.val = 0
        self.par = 0
        self.son_coin = 0
        self.sons = 1
        self.children = []


class Solution(object):
    def bonus(self, n, leadership, operations):
        """
        :type n: int
        :type leadership: List[List[int]]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        MOD = 1000000007
        tree = [node() for i in range(n+1)]

        for rel in leadership:
            tree[rel[1]].par = rel[0]
            #tree[rel[0]].sons += 1
            tree[rel[0]].children.append(rel[1])

        def update_sons(now):
            for son in tree[now].children:
                tree[now].sons += update_sons(son)
            return tree[now].sons


        def push_up(now, val):
            while now:
                tree[now].val += val
                tree[now].val %= MOD
                now = tree[now].par

        update_sons(1)
        ans = []
        for op in operations:

            if op[0] == 1:
                push_up(op[1], op[2])

            elif op[0] == 2:
                tree[op[1]].son_coin += op[2]
                tree[op[1]].son_coin %= MOD

                ret = tree[op[1]].sons*op[2]
                ret %= MOD
                #这里更新父节点的值，每个节点只有一个父节点，更新最高复杂度为深度
                push_up(op[1], ret)

            else:
                #这个地方要注意，不能每次都更新所有的子节点的值，可以一次性更新完
                ret = tree[op[1]].val
                par = tree[op[1]].par
                while par:
                    ret += tree[par].son_coin * tree[op[1]].sons
                    ret %= MOD
                    par = tree[par].par
                ans.append(ret)

        return ans


# class Solution:
#     def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
#         dicc = defaultdict(list)
#         dicf = {}
#         vals = [0]*(n+1)
#         for k,v in leadership:
#             dicc[k].append(v)
#             dicf[v]=k
#         # def helper(node):
#         #     if node not in dicc:
#         #         return []
#         #     else:
#         #         out = []
#         #         for c in dicc[node]:
#         #             out.append(c)
#         #             out.extend(helper(c))
#         #         dicallc[node] = out
#         #         return out
#         # helper(1)
#         def loopc(cur,val,cal=0):
#             vals[cur]+=val
#             if cur not in dicc:
#                 return 1
#             else:
#                 for x in dicc[cur]:
#                     cal += loopc(x,val,cal)
#                 vals[cur]+=(val*cal)
#                 return cal+1
#         out = []
#         for op in operations:
#             if op[0]==1:
#                 vals[op[1]]+=op[2]
#             elif op[0]==2:
#                 cur = op[1]
#                 val = op[2]
#                 cal = loopc(cur,val)
#                 while cur in dicf:
#                     cur = dicf[cur]
#                     vals[cur]+=cal*val
#             else:
#                 out.append(vals[op[1]])
#         return out


if __name__ == '__main__':
    so = Solution()
    N = 6
    leadership = [[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]]
    operations = [[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]
    print(so.bonus(N,leadership,operations))