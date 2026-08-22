# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dfs(node):
            if not node: return 0, 0
            rob_parent = 0
            left = dfs(node.left)
            right = dfs(node.right)
            rob_parent = node.val + left[1] + right[1]

            skip_parent = max(left) + max(right)
            return (rob_parent, skip_parent)
        return max(dfs(root))
            