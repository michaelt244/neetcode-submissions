# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#0 -> 1 -> 2 -> 3 -> 4 -> 5
#0 -> 1 -> 2 -> 3 -> 4 -> 5 (inital)
#0(prev) -> 1 -> 2 (temp)-> 3 -> 4 -> 5 (temp = curr.next)
#0 -> 1 <- 2 -> 3 -> 4 -> 5 (curr.next = prev)
#0 -> 1(prev) <- 2 -> 3 -> 4 -> 5 (prev = curr)
#0 -> 1(prev) <- 2 (curr)-> 3 -> 4 -> 5(curr = temp)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
       

        return curr.next


        