# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        n = TreeNode(val)
        if not root: return n
        temp = root
        
        while temp:
            if temp.val < val:
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = n
                    return root
            else:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = n
                    return root
        
