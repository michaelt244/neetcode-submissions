# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        # If the current node is None (we've reached beyond a leaf), 
        # there is nothing to swap, so we stop the recursion here.
        if not root:
            return
        
        # We swap the left child and the right child of the CURRENT node.
        root.left, root.right = root.right, root.left

        #now we do it for the childern as well 
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


