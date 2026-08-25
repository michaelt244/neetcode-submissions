# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0

            return 1 + max(dfs(node.left), dfs(node.right))
        
        current_max = 0

        current_max = max(current_max, dfs(root.right) + dfs(root.left))

        return current_max
        