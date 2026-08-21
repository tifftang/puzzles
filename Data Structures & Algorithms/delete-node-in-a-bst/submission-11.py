# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left and root.right:
                left = root.right
                while left.left:
                    left = left.left
                root.val = left.val
                root.right = self.deleteNode(root.right, root.val)
            elif root.left:
                root = root.left
            else:
                root = root.right
        return root
