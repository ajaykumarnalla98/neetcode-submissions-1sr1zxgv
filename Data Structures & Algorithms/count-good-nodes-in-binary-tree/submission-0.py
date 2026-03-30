# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, maxVal):
            nonlocal res
            if not node:
                return 0

            if node.val >= maxVal:
                res += 1
            
            new_max = max(maxVal, node.val)

            dfs(node.left, new_max)
            dfs(node.right, new_max)
        
        dfs(root, root.val)
        return res