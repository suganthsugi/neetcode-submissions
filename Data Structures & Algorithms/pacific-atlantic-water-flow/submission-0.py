class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i, j, visited):
            currVal = heights[i][j]
            directions = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]

            for i, j in directions:
                if i>=0 and j>=0 and i<len(heights) and j<len(heights[i]) and (i, j) not in visited and heights[i][j]>=currVal:
                    visited.add((i, j))
                    dfs(i, j, visited)
        
        visited1 = set([])
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if i==0 or j==0:
                    visited1.add((i, j))
                    dfs(i, j, visited1)
        
        visited2 = set([])
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if i==len(heights)-1 or j==len(heights[i])-1:
                    visited2.add((i, j))
                    dfs(i, j, visited2)
        result = visited1 & visited2
        return [list(r) for r in result]