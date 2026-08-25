# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        current_max = 0

        def dfs(node):
            # nonlocal allows us to update the current_max variable defined outside this function
            nonlocal current_max

            if not node:
                return 0
            
            # Recursively find the height of the left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # The diameter at the current node is the sum of the heights of its subtrees.
            # We update current_max if this local path is longer than any seen before.
            current_max = max(current_max, right + left)

            # Return the height of this node to its parent.
            # Height is 1 (the current node) + the height of the tallest child.

            return 1 + max(left, right)
        
        dfs(root)
        return current_max
        