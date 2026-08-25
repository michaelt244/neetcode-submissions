# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False

        def dfs(root1, root2):
            if not root1 and not root2:
                return True

            elif not root1:
                return False
            elif not root2:
                return False

            elif root1.val != root2.val:
                return False
            else:
                return dfs(root1.right, root2.right) and dfs(root1.left, root2.left)
            
        if root.val != subRoot.val:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

        else:
            return dfs(root, subRoot)
        
