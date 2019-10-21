#不完全背包，每个物品一个
# dp[i][j] = max(dp[i-1][j],dp[i-1][j-ws[i]]+vs[i])
def bag_p_2d(N,V,ws,vs):
    dp = [[float('-inf') if True else 0]*(V+1) for i in range(N+1)]
    for i in range(N+1):
        dp[i][0]=0
    for i in range(1,N+1):
        for j in range(ws[i-1],V+1):
            dp[i][j] = max(dp[i - 1][j], dp[i-1][j - ws[i-1]] + vs[i-1])
    return dp[-1][-1]

def bag_p_1d(N,V,ws,vs):
    dp = [0]*(V+1)
    for i in range(N):
        for j in range(V,ws[i]-1,-1):
            dp[j] = max(dp[j],dp[j-ws[i]]+vs[i])
    return dp[V]

#完全背包，每个物品可以很多个
def fullbag_p_2d(N,V,ws,vs):
    dp = [[float('-inf') if True else 0]*(V+1) for i in range(N+1)]
    for i in range(N+1):
        dp[i][0]=0
    for i in range(1,N+1):
        for j in range(ws[i-1],V+1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - ws[i-1]] + vs[i-1])
    return dp[-1][-1]

def coinc(coins,amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    for i in range(1,amount+1):
        for j in coins:
            dp[i] = min(dp[i],dp[i-j]+1)
    return dp[-1]


if __name__ == '__main__':
    # print(fullbag_p_2d(5,11,[4,2,3,5,5],[5,4,3,2,1]))
    print(coinc([1,2,5],11))
# 1                // 用例数
# 5 10             // 物品数 背包容量 N <= 1000 , V <= 1000
# 1 2 3 4 5        // w
# 5 4 3 2 1        // v
# 14