class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1 = len(s)
        l2 = len(p)
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        dp[0][0]=1
        for i in range(l2//2):
            if p[2*i+1]=='*':
                dp[0][2*i+2] = dp[0][2*i]
        for i in range(l1):
            for j in range(l2):
                if s[i] == p[j] or p[j]=='.':
                    dp[i+1][j+1]=dp[i+1][j+1] or dp[i][j]
                if p[j]=='*':
                    #这个地方应该这样思考，只要出现*就可以退两步，如果上一项相等，可以退一步
                    if p[j-1] == s[i] or p[j-1]=='.':
                        dp[i + 1][j + 1] = dp[i + 1][j + 1] or dp[i+1][j] or dp[i][j] or dp[i][j+1] or dp[i+1][j-1]
                    elif j>1:


                        dp[i + 1][j + 1] = dp[i + 1][j + 1] or dp[i+1][j-1]
        return dp[-1][-1]

if __name__ == '__main__':

    so =Solution()
    so.isMatch("aasdfasdfasdfasdfas",
               "aasdf.*asdf.*asdf.*asdf.*s")
