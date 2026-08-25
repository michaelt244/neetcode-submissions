# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        l1 = head
        l2 = head.next

        while l2 and l2.next:
            l2 = l2.next.next
            l1 = l1.next
        #l1 is in the midpoint

        #revese the second part of the list and beyond [half point] (treat l1 as the head)
        second = l1.next
        previous = l1.next = None

        while second:
            temp = second.next
            second.next = previous
            previous = second
            second = temp
        
        #now we have to fix the pointers
        first, second = head, previous

        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2



        
        