# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def bfs(node, depth=1):
            d1, d2 = depth, depth
            if node.right:
                d1=bfs(node.right, depth+1)
            if node.left:
                d2=bfs(node.left, depth+1)
            return max(d1, d2)
        
        return bfs(root)