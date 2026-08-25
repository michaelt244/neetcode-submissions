# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        #making a helper function to append the values to the list

        def inorder(node):
            #return when no more leaf nodes
            if not node:
                return

            #left side leafs then middle then right side leafs
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
    
        inorder(root)
        return res
