class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseOrder = []
        learned = set([])

        preMap = {i: [] for i in range(numCourses)}
        for c, preq in prerequisites:
            preMap[c].append(preq)
        
        def dfs(currC, visited=set([])):
            if preMap[currC]==[]:
                if currC not in learned:
                    learned.add(currC)
                    courseOrder.append(currC)
                return True
            if currC in visited: return False

            visited.add(currC)
            
            for xc in preMap[currC]:
                if not dfs(xc, visited): return False
            
            preMap[currC] = []
            visited.remove(currC)
            if currC not in learned:
                learned.add(currC)
                courseOrder.append(currC)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []

        return courseOrder
