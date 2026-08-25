# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1:
                return False
            elif not root2:
                return False
            else:
                return root1.val == root2.val
            

        return dfs(p.right, q.right) and dfs(p.left, q.left)
    
        