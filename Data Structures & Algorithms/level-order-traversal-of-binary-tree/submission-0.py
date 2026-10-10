# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelMap = {}
        totalLevels = 0
        def dfs(node, level = 0):
            nonlocal totalLevels
            if not node:
                return
            
            if level in levelMap:
                levelMap[level].append(node.val)
            else:
                levelMap[level] = [node.val]
                totalLevels+=1
            
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root)
        result = []
        for i in range(0, totalLevels):
            result.append(levelMap[i])

        return result