# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()
        res = []

        if root:
            queue.append(root)

        # Continue processing as long as there are nodes in the queue
        while len(queue) > 0:
            #creating a temporay list for the current level
            current_level = []

            for i in range(len(queue)):
                #pop the current node
                curr = queue.popleft()
                #append that node to the temporay level
                current_level.append(curr.val)

                #if there are leaf nodes add them to the queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            #at the end append the nodes at that level (works as range(len(queue)) takes a snap shot of the current lenght so the addition levels do not affect the snapshot)
            res.append(current_level)        
        return res