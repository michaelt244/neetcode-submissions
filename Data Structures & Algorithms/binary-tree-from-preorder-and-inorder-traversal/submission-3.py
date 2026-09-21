# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        #pre order (root -> left -> right)
        #in order (left -> root -> right)

        #first value in the preorder list is the split between the left and right tree
        root_val = preorder[0]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)


        # we build the left side of the tree which is all the values left of the mid point
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])

        # we then build the rihgt side of the tree which is all the values right of the mid point
        root.right = self.buildTree(preorder[mid + 1: ], inorder[mid + 1:])

        return root