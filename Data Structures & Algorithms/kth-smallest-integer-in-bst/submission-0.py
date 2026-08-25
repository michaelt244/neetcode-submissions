# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    

        def search(node) -> int:
            if not node:
                return 1
                
            search(node.left)
            cnt[0] += 1
            if cnt[0] == k:
                return node.val
            else:
                return search(node.right)
        
        cnt = [0]
        kth_smallest = search(root)

        return kth_smallest