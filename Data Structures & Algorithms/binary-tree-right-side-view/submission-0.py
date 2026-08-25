# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()

        if root:
            queue.append(root)
        
        right_side = []
        while len(queue) > 0:
            end = len(queue)
            for i in range(end):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right) 
                if i == end - 1:
                    right_side.append(curr.val)
                        

        return right_side

        