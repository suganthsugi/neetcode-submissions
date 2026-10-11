class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            preMap[i].append(j)

        def dfs(curr, visited):
            if preMap[curr] == []: return True
            if curr in visited:
                return False
            
            visited.add(curr)
            for x in preMap[curr]:
                if not dfs(x, visited): return False
            preMap[curr] = []
            visited.remove(curr)
            return True
        
        for i in range(numCourses):
            if not dfs(i, set([])): return False
        
        return True