# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        if not root:
            return result
        
        def dfs(node):
            nonlocal result
            if node.right:
                l1 = dfs(node.right)
            else:
                l1 = 0
            if node.left:
                l2 = dfs(node.left)
            else:
                l2 = 0
            result = max(result, l1+l2)
            return max(l1, l2)+1
        
        dfs(root)
        return result