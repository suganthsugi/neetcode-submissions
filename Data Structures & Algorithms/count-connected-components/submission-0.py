class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set([])
        result = 0
        mapping = { i: [] for i in range(n) }
        for i, j in edges:
            mapping[i].append(j)
            mapping[j].append(i)

        def dfs(i, prev = None):
            if i in visited or mapping[i] == []: return
            visited.add(i)

            for x in mapping[i]:
                if x == prev: continue
                dfs(x, i)
            
            mapping[i]=[]
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                result+=1
        return result