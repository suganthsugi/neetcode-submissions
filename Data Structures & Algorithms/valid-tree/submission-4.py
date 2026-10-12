class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mapping = {i:[] for i in range(n)}
        for i, j in edges:
            mapping[i].append(j)
            mapping[j].append(i)
        
        visited = set([])

        def dfs(i, prev = None):
            if i in visited:
                return False
            visited.add(i)
            if mapping[i] == []: return True

            for x in mapping[i]:
                if x==prev: continue
                if not dfs(x, i): return False
            mapping[i] = []
            return True
        for i in range(n):
            if i in visited: continue
            visited = set([])
            if not dfs(i) or len(visited) != n: return False
        return True