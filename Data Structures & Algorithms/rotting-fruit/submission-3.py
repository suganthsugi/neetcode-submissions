class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(q):
            result = 0
            while len(q) > 0:
                i, j, time = q.popleft()

                directions = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]

                for i, j in directions:
                    if i>=0 and i<len(grid) and j>=0 and j<len(grid[i]) and grid[i][j]==1:
                        result = max(result, time+1)
                        q.append((i, j, time+1))
                        grid[i][j] = -1
            return result
        
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    q.append((i, j, 0))

        result = bfs(q)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    return -1
        return result