class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            q = deque([])
            q.append((i, j))

            while len(q)>0:
                i, j = q.popleft()

                directions = [[i+1, j], [i-1, j], [i, j-1], [i, j+1]]

                for i, j in directions:
                    if i>=0 and j>=0 and i<len(grid) and j<len(grid[i]) and grid[i][j] == '1':
                        grid[i][j]='-1'
                        q.append((i, j))

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    bfs(i, j)
                    result+=1
        return result