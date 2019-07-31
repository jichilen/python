from typing import List
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if len(grid)==0:return
        visited = [[0]*len(grid) for _ in range(len(grid[0]))]
        visiting = [[grid[0][0],[0,0]]]
        result = 0
        cal = 0
        while len(visiting)>0:
            val,(x,y) = heapq.heappop(visiting)
            cal +=1
            visited[x][y]=cal
            result = max(result,val)
            if x == len(grid) - 1 and y == len(grid[0]) - 1: break
            for i, j in [(0,1),(0,-1),(-1,0),(1,0)]:
                if x+i>=0 and x+i<len(grid) and y+j>=0 and y+j<len(grid[0]) and visited[x+i][y+j] == 0:
                    heapq.heappush(visiting,[grid[x+i][y+j],[x+i,y+j]])

        return result


if __name__ == '__main__':
    so = Solution()
    so.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])

