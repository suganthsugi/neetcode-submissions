class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def bfs(i, j, pos = 0):

            q = deque([(i, j, pos)])

            while len(q)>0:
                i, j, pos = q.popleft()

                directions = [[i+1, j], [i-1, j], [i, j-1], [i, j+1]]

                for i, j in directions:
                    if i>=0 and j>=0 and i<len(grid) and j<len(grid[i]):
                        if(grid[i][j]>0 and grid[i][j]>pos+1):
                            q.append((i, j, pos+1))
                            grid[i][j] = pos+1
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    bfs(i, j)
        
