class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0: continue
                directions = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]

                for k, l in directions:
                    if k>=0 and l>=0 and k<len(grid) and l<len(grid[i]):
                        if grid[k][l] == 0:
                            result+=1
                    else:
                        result+=1
        return result