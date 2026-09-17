# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

    
        dummy = ListNode()
        tail = dummy


        heap = []
        heapq.heapify(heap) 

        #adding the first layer + using a counter since a tie will need a second value to tell what comes after as node_a < node_b is not defined
        counter = 0
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1
        
        while heap:
            _, _ , node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            #if there is next value in the list add the next number to the heap is not skip to the next number
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1
            
        return dummy.next




        