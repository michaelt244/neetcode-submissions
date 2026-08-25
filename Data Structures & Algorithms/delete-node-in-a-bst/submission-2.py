# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            #we found the target
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                #hard case when there is 2 leaf nodes, find the min and replace the node with it
                root.val = self.findmin(root.right).val
                root.right = self.deleteNode(root.right, root.val)         
        return root


    


    def findmin(self, root) -> root:
        curr = root
        #going down the left and finding the smallest value
        while curr and curr.left:
            curr = curr.left
        return curr
