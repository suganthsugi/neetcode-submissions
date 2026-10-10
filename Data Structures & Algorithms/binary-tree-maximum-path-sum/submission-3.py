# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')
        def dfs(node):
            if not node:return 0
            nonlocal result

            lsum = dfs(node.left)
            rsum = dfs(node.right)

            currRes = max(0, lsum)+max(0, rsum)+node.val
            result = max(currRes, result)

            t1=node.val+lsum
            t2=node.val+rsum
            path = max(node.val, t1, t2)            
            
            
            return path
        
        dfs(root)
        return result