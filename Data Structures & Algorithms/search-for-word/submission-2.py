class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False

        def dfs(i, j, ind, visited):
            nonlocal result
            if ind == len(word):
                result = True
                return

            directions = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
            for i, j in directions:
                if i>=0 and j>=0 and i<len(board) and j<len(board[i]) and (i, j) not in visited and board[i][j] == word[ind]:
                    visited.add((i, j))
                    dfs(i, j, ind+1, visited)
                    visited.remove((i, j))
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==word[0]:
                    dfs(i, j, 1, set([(i, j)]))
        return result