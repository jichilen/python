class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag = 0
        if n==0:return 1
        if n<0:
            flag = 1
            n = -n
        def helper(x,n):
            if n==0:return 1
            if n==1:
                return x
            tmp = helper(x,n//2)
            if n&1==1:
                return tmp*tmp*x
            return tmp*tmp
        out = helper(x,n)
        if flag:
            return 1/out
        return out

if __name__ == '__main__':
    so = Solution()
    print(so.myPow(2.0,10))
    print(so.myPow(2.0,-10))
    print(so.myPow(2.0,9))
    print(so.myPow(1.5,3))
