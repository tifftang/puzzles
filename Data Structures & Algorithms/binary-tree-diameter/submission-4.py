# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0

        def traverse(node):
            if not node: return 0
            left = traverse(node.left)
            right = traverse(node.right)
            self.longest = max(self.longest, (left + right))
            return max(left, right) + 1
        traverse(root)
        return self.longest