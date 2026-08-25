# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(root, max_value):
            if not root:
                return True
            
            if root.left:
                return (root.left, root.value)
            if root.right:
                return (root.right, root.value)
            if root.val > max_value:
                return True
            else:
                return False
        
        return dfs(root, root.val)
