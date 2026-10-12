class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set([])
        mapping = {}
        result = []
        for i, j in edges:
            if i in mapping:
                mapping[i].append(j)
            else:
                mapping[i] = [j]
            if j in mapping:
                mapping[j].append(i)
            else:
                mapping[j] = [i]
        
        def dfs(i, v, prev=None):
            nonlocal result
            if result != []: return result
            if i in v:
                loop = []
                tloop=True
                for tt in range(len(v)-1, -1, -1):
                    if tloop: loop.append(v[tt])
                    if v[tt] == i:
                        tloop=False
                v=loop 
                for t in range(len(edges)-1, -1, -1):
                    t1, t2 = edges[t]
                    if t1 in v and t2 in v:
                        result = [t1, t2]
                        return
            if mapping[i] == []: return
            if i in visited: return
            
            visited.add(i)
            v.append(i)

            for x in mapping[i]:
                if x!= prev: dfs(x, v, i)
            
            v.pop()
            mapping[i] = []
        
        dfs(1, [])
        return result