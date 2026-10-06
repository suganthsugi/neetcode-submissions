class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result = False
        def dfs(i, j):
            nonlocal result
            visited = set([])
            stk = deque([(i, j)])
            while len(stk)>0:
                i, j = stk.popleft()
                if matrix[i][j] == target:
                    result = True
                    return
                if i+1<len(matrix) and matrix[i+1][j]<=target and (i+1, j) not in visited:
                    stk.append((i+1, j))
                    visited.add((i+1, j))
                if j+1<len(matrix[i]) and matrix[i][j+1]<=target and (i, j+1) not in visited:
                    stk.append((i, j+1))
                    visited.add((i, j+1))
        
        dfs(0, 0)
        return result