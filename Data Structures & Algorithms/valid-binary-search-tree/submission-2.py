# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lmax, rmax):
            if not node:
                return True
            
            if node.val<=lmax or node.val>=rmax:
                return False

            l = dfs(node.left, lmax, node.val)
            r = dfs(node.right, node.val, rmax)  
            return (l and r)
        
        return dfs(root, float('-inf'), float('inf'))