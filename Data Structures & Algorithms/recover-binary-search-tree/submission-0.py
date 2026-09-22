# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        arr = []

        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            arr.append(node)
            inorder(node.right)
        
        print(arr)