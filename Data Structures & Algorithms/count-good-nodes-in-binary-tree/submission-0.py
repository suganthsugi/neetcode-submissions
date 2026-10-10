# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def dfs(node, cMax = float('-inf')):
            if not node: return

            nonlocal result
            if node.val>=cMax:
                result+=1
            
            dfs(node.left, max(cMax, node.val))
            dfs(node.right, max(cMax, node.val))
        
        dfs(root)
        return result