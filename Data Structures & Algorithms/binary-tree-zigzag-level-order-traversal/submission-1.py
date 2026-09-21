# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()
        

        if not root:
            return []

        queue.append(root)
        result = []
        level = 0
        
        while queue:
            order = []
            for i in range(len(queue)):
                
                current = queue.popleft()
                order.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                
                if level % 2 == 1:
                    order.reverse()
                    
            level += 1
            result.append(order)        
        return result
            
        

        


        