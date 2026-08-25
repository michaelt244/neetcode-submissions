# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        cnt = 0
        result = root.val

        def search(node):
            #allowing us to acceses the cnt and result varibales
            nonlocal cnt, result

            #once we reach the null go back up
            if not node:
                return
            

            #go down all the way to the smallest number

            search(node.left)
            #if we reached the kth smallest value return the value
            if cnt == k:
                return
            cnt += 1
            if cnt == k:
                result = node.val
                return
            
            search(node.right)
    
        search(root)
        return result