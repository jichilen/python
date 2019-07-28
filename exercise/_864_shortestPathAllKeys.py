from typing import List
from collections import deque
#这是一个典型的搜索的问题，问题的难点在于可以回头，但是不能随时回头
#每次拿到钥匙之后就可以回头
#可以将问题化为，从钥匙到下一个钥匙的问题，拿到钥匙之后就更新地图，由于不用递归，所以不能原地更新地图，需要额外的空间辅助
#先考虑最简单的广度优先搜索
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        #找到起点，钥匙数量，以及他们的名字
        keydic = {}
        expanding = deque()
        expanded = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    expanding.append([0,i,j,0])
                    expanded.add((i,j,0))
                elif grid[i][j]!='.' and grid[i][j] !='#':
                    keydic[grid[i][j]] = [i, j]
        keylist = {}
        cal = 0
        for key in keydic:
            if not key.lower() in keylist:
                keylist[key.lower()] = cal
                cal+=1
        keynum = len(keylist)
        #if two keys, the status are b0 b1 b10 b11
        finalstatus = 0
        for i in range(keynum):
            finalstatus<<=1
            finalstatus+=1
        search_d = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while len(expanding)>0:
            step,i,j,status = expanding.popleft()
            for dx,dy in search_d:
                if i+dx<0 or dx+i>len(grid)-1 or j+dy<0 or j+dy>len(grid[0])-1 or grid[i+dx][j+dy]=='#' :
                    continue
                if (i+dx,j+dy,status) in expanded :
                    continue
                status_n = status
                if grid[i+dx][j+dy] in keylist:
                    #这里有个隐藏的陷阱，重复走过钥匙节点不应该再次更新
                    val=pow(2,keylist[grid[i+dx][j+dy]])
                    if val&status_n!=val:
                        status_n+=val
                elif grid[i+dx][j+dy] in keydic:
                    val = pow(2,keylist[grid[i+dx][j+dy].lower()])
                    if val&status_n!= val:
                        continue
                if status_n == finalstatus:
                    return step + 1
                expanded.add((i+dx,j+dy,status_n))
                expanding.append([step+1,i+dx,j+dy,status_n])
        return -1

    def shortestPathAllKeys1(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        door_key = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f'}
        key_map = {}
        key_num = 0
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    queue.append([0, i, j, 0])
                elif grid[i][j] in door_key.values():
                    key_map[grid[i][j]] = key_num
                    key_num += 1
        final_status = (1 << key_num) - 1
        visited = set()
        visited.add((i, j, 0))
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while True:
            if len(queue) == 0:
                return -1
            step, i, j, status = queue.pop(0)
            if status == final_status:
                return step
            for d in directions:
                new_i = i + d[0]
                new_j = j + d[1]
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]):
                    continue
                c = grid[new_i][new_j]
                if c == '#' or (c in door_key and (status & (1<<key_map[door_key[c]])) == 0):
                    continue
                new_status = status
                if c in key_map:
                    new_status = status | (1<<key_map[c])
                if (new_i, new_j, new_status) not in visited:
                    visited.add((new_i, new_j, new_status))
                    queue.append((step+1, new_i, new_j, new_status))



if __name__ == '__main__':
    map = ["@.a.#",
           "###.#",
           "b.A.B"]
    map1 = ["..#....##.",
            "....d.#.D#",
            "#...#.c...",
            "..##.#..a.",
            "...#....##",
            "#....b....",
            ".#..#.....",
            "..........",
            ".#..##..A.",
            ".B..C.#..@"]
    map2 = ["#..#.#.#..#.#.#.....#......#..",
            ".#.......#....#A.....#.#......",
            "#....#.....#.........#........",
            "...#.#.........#..@....#....#.",
            ".#.#.##...#.........##....#..#",
            "..........#..#..###....##..#.#",
            ".......#......#...#...#.....c#",
            ".#...#.##......#...#.###...#..",
            "..........##...#.......#......",
            "#...#.........a#....#.#.##....",
            "..#..#...#...#..#....#.....##.",
            "..........#...#.##............",
            "...#....#..#.........#..D.....",
            "....#E.#....##................",
            "...........##.#.......#.#....#",
            "...#..#...#.#............#e...",
            "..#####....#.#...........##..#",
            "##......##......#.#...#..#.#..",
            ".#F.......#..##.......#....#..",
            "............#....#..#..#...#..",
            ".............#...#f...#..##...",
            "....#..#...##.........#..#..#.",
            ".....#.....##.###..##.#......#",
            ".#..#.#...#.....#........###..",
            ".....#.#...#...#.....#.....#..",
            "##.....#....B.....#..#b.......",
            ".####....##..#.##..d.#......#.",
            "..#.....#....##........##...##",
            "...#...#...C..#..#....#.......",
            "#.....##.....#.#......#......."]
    so = Solution()
    print(so.shortestPathAllKeys(map2))
    print(so.shortestPathAllKeys1(map2))
