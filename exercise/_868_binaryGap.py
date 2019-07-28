class Solution:
    def binaryGap(self, N: int) -> int:
        lastmax = 0
        last_o = -1
        cal = 0
        while N>0:
            cal += 1
            if N&1 ==1:
                if last_o>=0:
                    lastmax = max(lastmax,cal-last_o)
                last_o=cal
            N=N>>1
        return lastmax


if __name__ == '__main__':
    so = Solution()
    print(so.binaryGap(19))