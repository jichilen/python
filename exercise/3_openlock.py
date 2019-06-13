from collections import deque


class Solution:
    def openLock(self, deadends, target: str) -> int:
        deadends = [tuple([int(i) for i in dead]) for dead in deadends]
        deadends = set(deadends)
        target = [int(i) for i in target]
        exploring = deque()
        nexploring = deque()
        exploring.append([0, 0, 0, 0])
        exploded = set()
        cal = 0
        while len(exploring) != 0 or len(nexploring) != 0:
            cal += 1
            while len(exploring) != 0:
                st = exploring.popleft()
                if tuple(st) in exploded:
                    continue
                if tuple(st) in deadends:
                    continue
                if st == target:
                    return cal - 1
                exploded.add(tuple(st))
                for i in range(4):
                    for j in [-1, 1]:
                        tmp = st.copy()
                        tmp[i] += j
                        if tmp[i] < 0:
                            tmp[i] = 9
                        elif tmp[i] > 9:
                            tmp[i] = 0
                        if tuple(tmp) in exploded:
                            continue
                        if tmp in exploring:
                            continue
                        nexploring.append(tmp)
            nexploring, exploring = exploring, nexploring
        return -1


if __name__ == '__main__':
    init = '0000'
    deadends = ["1131", "1303", "3113", "0132", "1301", "1303", "2200", "0232", "0020", "2223"]
    target = "3312"
    so = Solution()
    re = so.openLock(deadends, target)
    print(re)
# TODO:这个题应该用DFS来解要好很多