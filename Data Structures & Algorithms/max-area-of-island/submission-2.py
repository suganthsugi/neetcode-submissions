class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, area = 1):
            grid[i][j] = -1

            directions = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]

            for i, j in directions:
                if(i>=0 and j>=0 and i<len(grid) and j<(len(grid[i])) and grid[i][j]==1):
                    area += dfs(i, j)
            
            return area
        

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    result = max(result, dfs(i, j))
        
        return result