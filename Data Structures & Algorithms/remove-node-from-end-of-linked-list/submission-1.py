# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #making a dummycase for the n ==1 edge case
        dummy = ListNode(0, head)
        tracer = dummy
        previous = dummy
        
        #get the tracer to the nth spot
        for i in range(n + 1):
            tracer = tracer.next

        #then increase both the tracer + prevous pointer till the tracer is null
        #this creates a gap that causes the previous pointer to be one step away
        #from the node we need to delete
        while tracer:
            tracer = tracer.next
            previous = previous.next
        
        #then we delete the node (previou.next)
        temp = previous.next.next
        previous.next = temp

        #return everything after the dummynode
        return dummy.next



        