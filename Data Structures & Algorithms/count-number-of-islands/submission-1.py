class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def go(i, j):
            grid[i][j] = '-1'
            if i-1>=0 and grid[i-1][j]=='1':
                go(i-1, j)
            if i+1<len(grid) and grid[i+1][j]=='1':
                go(i+1, j)
            if j-1>=0 and grid[i][j-1]=='1':
                go(i, j-1)
            if j+1<len(grid[i]) and grid[i][j+1]=='1':
                go(i, j+1)

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    go(i, j)
                    result+=1
        return result