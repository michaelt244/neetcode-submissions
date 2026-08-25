# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def pathfinder(root, path, count):
            if not root:
                return False
            
            path.append(root.val)
            count += root.val
            if not root.left and not root.right:
                if count == targetSum:
                    return True
                else:
                    return False
            if pathfinder(root.left, path, count):
                return True
            if pathfinder(root.right, path, count):
                return True
            path.pop()
            count -= root.val

            return False
        
        ans1 = 0
        ans2 = []
        return pathfinder(root, ans2, ans1)



        