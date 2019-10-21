class Solution:
    def __init__(self):
        self.dp = []

    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[float('inf')] * (N + 1) for _ in range(K + 1)]
        for j in range(1, N + 1):
            dp[0][j] = 0
            dp[1][j] = j
        for i in range(1, K + 1):
            dp[i][0] = 0
            dp[i][1] = 1
        l1 = len(self.dp)
        if l1 > 0:
            l2 = len(self.dp[0])
        else:
            l2 = 0
        for i in range(2,K+1):
            for j in range(1,N+1):
                if l1>0 and i<l1 and j<l2:
                        dp[i][j] = self.dp[i][j]
                else:
                    for m in range(1,j+1):
                        dp[i][j] = min(dp[i][j],max(dp[i-1][m-1],dp[i][j-m])+1)
        if K+1>=l1 and N+1>=l2:
            self.dp = dp
        return dp[-1][-1]


if __name__ == '__main__':
    so = Solution()
    print(so.superEggDrop(2,6))
    print(so.superEggDrop(1,3))
    print(so.superEggDrop(3,14))
    print(so.superEggDrop(4, 5000))