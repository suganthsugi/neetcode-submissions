# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        result = False
        

        def dfs(node):
            if not node:
                return
            nonlocal result
            if node.val == subRoot.val:
                currRes = True
                def sameTree(t1, t2=subRoot):
                    nonlocal currRes
                    if (t1 and not t2) or (t2 and not t1) or (t1 and t2 and t1.val != t2.val):
                        currRes = False
                        return
                    if t1 and t2:
                        sameTree(t1.left, t2.left)
                        sameTree(t1.right, t2.right)
                sameTree(node)
                if currRes:
                    result = True
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result