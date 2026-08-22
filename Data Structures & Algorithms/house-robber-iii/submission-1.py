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
        def dfs(node, skip):
            if not node: return 0
            rob_parent = 0
            if not skip:
                rob_parent = node.val + dfs(node.left, True) + dfs(node.right, True)
            left = dfs(node.left, False)
            right = dfs(node.right, False)
            skip_parent = left + right
            #print(node.val, rob_parent, skip_parent, skip)
            return max(rob_parent, skip_parent)
        return max(dfs(root, True), dfs(root, False))
            