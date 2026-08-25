# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        #val is bigger than the node so go right
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        #val is smaller than the node so go left
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        
        return root
    




        