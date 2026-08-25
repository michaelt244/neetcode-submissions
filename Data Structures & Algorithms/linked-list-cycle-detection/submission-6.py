# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
         

        #targets edge cases such as []
        if fast is None:
            return False

        #if 1 (fast) -> null (fast.next) 
        #or  1 (fast) -> 2 (fast.next) -> null (fast.next.next)
        #this means this is not a cycle as it comes to an end
        while fast.next and fast.next.next:
            fast = fast.next.next #increment by 2
            #if fast == slow then there is cycle as the fast will eventually
            #equal the slower point as thier is a cycle that brings them closer and clsoe
            if fast == slow:
                return True
            slow = slow.next #increment by 1

        #no cycle detected as we got a null
        return False
        