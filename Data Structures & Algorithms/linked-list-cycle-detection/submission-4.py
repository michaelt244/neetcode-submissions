# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        if fast is None:
            return False

        while fast.next and fast.next.next:
            fast = fast.next.next
            if fast == slow:
                return True
            slow = slow.next
        return False
        