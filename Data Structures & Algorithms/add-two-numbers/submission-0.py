# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        total = []
        carry = 0
        while l1 or l2 or carry:

            #initialy carry = 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum_val = (v1 + v2 + carry)

            if sum_val >= 10:
                carry = sum_val // 10
                sum_val = sum_val % 10
                total.append(sum_val)
                l1 = l1.next
                l2 = l2.next
                continue
                
            carry = 0
            total.append(sum_val)
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        dummy = ListNode()
        tail = dummy

        for i in range(len(total)):
            tail.next = ListNode(total[i])
            tail = tail.next
        
        return dummy.next
        


