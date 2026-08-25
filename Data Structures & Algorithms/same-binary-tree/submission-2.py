# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(root1, root2):

            # Base cases: handle Nones
            if not root1 and not root2:
                return True

            elif not root1:
                return False
            elif not root2:
                return False

            # Check current values
            elif root1.val != root2.val:
                return False
            # If values match, the answer depends on the children
            else:
                return dfs(root1.right, root2.right) and dfs(root1.left, root2.left)
        
        return dfs(p, q)
    
        