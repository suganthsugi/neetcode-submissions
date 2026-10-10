# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True
        

        def dfs(node):
            nonlocal result
            if node is None or not result:
                return 0
            l1 = dfs(node.left)
            l2 = dfs(node.right)
                
            if abs(l1-l2)>1:
                result = False
            
            return max(l1, l2) + 1
        
        dfs(root)
        return result