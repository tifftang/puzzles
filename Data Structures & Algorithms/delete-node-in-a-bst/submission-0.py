# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root
        insert = None
        def dfs(node, parent, d):
            nonlocal insert
            if not node: return
            if node.val == key:
                print(node.val, d)
                if node.left and node.right:
                    insert = node.right
                    if d == "l": parent.left = node.left
                    else: parent.right = node.left
                elif node.left:
                    if d == "l": parent.left = node.left
                    else: parent.right = node.left
                elif node.right:
                    if d == "l": parent.left = node.right
                    else: parent.right = node.right
                else:
                    if d == "l": parent.left = None
                    else: parent.right = None
            elif node.val < key:
                dfs(node.right, node, "r")
            else:
                dfs(node.left, node, "l")
        if root.val != key:
            dfs(root, None, "l")
        else:
            if root.left:
                insert = root.right
                root = root.left
            else:
                root = root.right
        if insert:
            tmp = root
            while tmp:
                if tmp.val < insert.val:
                    if tmp.right:
                        tmp = tmp.right
                    else:
                        tmp.right = insert
                        return root
                else:
                    if tmp.left:
                        tmp = tmp.left
                    else:
                        tmp.left = insert
                        return root
        return root