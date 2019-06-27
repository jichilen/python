def possum(x):
    out = 0
    while (x >= 10):
        out += x % 10
        x = x // 10
    return out + x


def mov_helper(r, c, m, n, k, visited):
    if r < 0 or c < 0 or r >= m or c >= n:
        return
    if possum(r) + possum(c) > k:
        return
    if visited[r][c] > 0:
        return
    visited[r][c] = 1
    mov_helper(r - 1, c, m, n, k, visited)
    mov_helper(r + 1, c, m, n, k, visited)
    mov_helper(r, c - 1, m, n, k, visited)
    mov_helper(r, c + 1, m, n, k, visited)
def rotbot_mov(m,n,k):
    if m<=0 or n<=0:
        return 0
    visited = [[0 for _ in range(n)] for _ in range(m)]
    mov_helper(0,0,m,n,k,visited)
    print(visited)
    return sum([sum(i) for i in visited])

if __name__ == '__main__':
    m=12
    n=12
    k=12
    print(rotbot_mov(m,n,k))