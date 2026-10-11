"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {}
        if not node:
            return None

        def dfs(curr = node):
            if curr not in mapping:
                mapping[curr] = Node(curr.val)
            
            for x in curr.neighbors:
                if x not in mapping:
                    dfs(x)
        
        dfs()
        for k in mapping.keys():
            v = mapping[k]
            for x in k.neighbors:
                v.neighbors.append(mapping[x])
        return mapping[node]