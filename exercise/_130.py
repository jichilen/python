from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m==0:return
        n = len(board[0])
        def dfs(board,i,j,m,n):
            if i<0 or i>=m or j<0 or j>=n or board[i][j]!='O':
                return
            board[i][j]='1'
            for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                dfs(board,i+dx,j+dy,m,n)

        for i in range(m):
            if i > 0 and i < m - 1:
                dfs(board, i, 0, m, n)
                dfs(board, i, n - 1, m, n)
            else:
                for j in range(n):
                    dfs(board,i,j,m,n)
        for i in range(m):
            for j in range(n):
                if board[i][j]!='1':
                    board[i][j]='X'
                else:
                    board[i][j] = 'O'
        return board

if __name__ == '__main__':
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    so = Solution()
    print(so.solve(board))