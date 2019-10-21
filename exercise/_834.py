from typing import List
import collections
class Solution:
    # time out
    # def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
    #     out = []
    #     for i in range(N):
    #         expanding = [i]
    #         nexpanding = []
    #         expanded=set()
    #         tmpr = 0
    #         cal = 0
    #         while len(expanding)>0:
    #             cal += 1
    #             for x in expanding:
    #                 expanded.add(x)
    #                 for e in edges:
    #                     if x == e[0] and e[1] not in expanded:
    #                         nexpanding.append(e[1])
    #                     elif x==e[1] and e[0] not in expanded:
    #                         nexpanding.append(e[0])
    #                     else:
    #                         continue
    #                     tmpr +=cal
    #             expanding = nexpanding
    #             nexpanding = []
    #         out.append(tmpr)
    #     return out
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N
        ans = [0] * N

        def dfs(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return ans




if __name__ == '__main__':
    so = Solution()
    N = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    print(so.sumOfDistancesInTree(N,edges))