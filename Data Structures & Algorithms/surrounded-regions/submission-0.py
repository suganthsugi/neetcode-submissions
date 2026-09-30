class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(i, j):
            if board[i][j] == 'O':
                board[i][j]='-'
                
                directions = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]

                for i, j in directions:
                    if i>=0 and j>=0 and i<len(board) and j<len(board[i]):
                        dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if i==0 or j==0 or i==len(board)-1 or j==len(board[i])-1:
                    dfs(i, j)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='-':
                    board[i][j]='O'
        