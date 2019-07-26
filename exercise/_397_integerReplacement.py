class Solution:
    def integerReplacement(self, n: int) -> int:
        cal = 0
        while n>1:
            if n&1==0:
                cal+=1
            elif n&2 ==2 and n!=3:
                cal+=2
                n = n+1
            else:
                cal+=2
            n = n>>1
        return cal

if __name__ == '__main__':
    so = Solution()
    print(so.integerReplacement(3))
