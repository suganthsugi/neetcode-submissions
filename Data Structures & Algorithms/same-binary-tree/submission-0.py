# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result = True

        def dfs(n1, n2):
            nonlocal result
            if not result: return
            if n1 is None and n2 is None:
                return
            if n1 is None and n2 is not None:
                result = False
                return
            if n1 is not None and n2 is None:
                result = False
                return
            if n1.val!=n2.val:
                result = False
                return
            
            dfs(n1.left, n2.left)
            dfs(n1.right, n2.right)
        
        dfs(p, q)
        return result