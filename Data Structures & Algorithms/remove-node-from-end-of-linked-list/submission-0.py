# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        tracer = dummy
        previous = dummy
        
        for i in range(n + 1):
            tracer = tracer.next

        while tracer:
            tracer = tracer.next
            previous = previous.next
        
        temp = previous.next.next
        previous.next = temp

        return dummy.next



        