class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def fac(n):
            out = 9
            for i in range(n-1):
                out = out*(9-i)
            return out
        out = 0
        for i in range(n):
            out += fac(i+1)
        return out+1

if __name__ == '__main__':

    so=Solution()
    print(so.countNumbersWithUniqueDigits(3))