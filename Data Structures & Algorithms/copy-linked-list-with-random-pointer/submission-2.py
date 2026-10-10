"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        nodeMap = {}
        t = head
        while t:
            newNode = Node(t.val)
            nodeMap[t] = newNode
            t = t.next
        
        for x in nodeMap.keys():
            currNode = nodeMap[x]
            currNode.next = nodeMap[x.next] if x.next else None
            currNode.random = nodeMap[x.random] if x.random else None
        
        return nodeMap[head]