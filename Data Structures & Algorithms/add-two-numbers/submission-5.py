# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        total = []
         #initialy carry = 0
        carry = 0
        while l1 or l2 or carry:

            #if there is a vlaue take the digit else use a 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #get the sum (v1 + v2 + carry(if threre is one))
            sum_val = (v1 + v2 + carry)

            #get the last digit and append it
            digit = sum_val % 10

            #the carry is the remaining digit left
            carry = sum_val //10

            #append the digit(if the digit is less than 10 it will remain the same(9%10 = 9))
            total.append(digit)

            #append the list if there is a next
            if l1: l1 = l1.next
            if l2: l2 = l2.next


        #build a new linklist
        dummy = ListNode()
        tail = dummy

        #build the remainding of the link list
        for i in range(len(total)):
            tail.next = ListNode(total[i])
            tail = tail.next
        
        return dummy.next
        


