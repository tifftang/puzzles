# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(node, max_seen):
            if not node: return 0
            good = 0
            if node.val >= max_seen:
                good += 1
                max_seen = node.val
            good += dfs(node.left, max_seen)
            good += dfs(node.right, max_seen)
            return good
        return dfs(root, -float('inf'))