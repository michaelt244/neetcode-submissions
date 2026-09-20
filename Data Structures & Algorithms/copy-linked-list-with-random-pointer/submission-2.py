"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # we initalize the mapping {old link : new link}
        seen = {None: None}

        curr = head
        # running throguht the link and mapping it to itslef
        # We walk through the entire original list
        # For each node, we create a Node with the same value.
        while curr:
            copy = Node(curr.val)
            seen[curr] = copy
            curr = curr.next

        curr = head
        # For each original node, we fetch its copy (copy).
        # We set: copy.next → look up the copy of curr.next in the dictionary.
        # copy.random → look up the copy of curr.random in the dictionary.
        # because oldToCopy contains every original node (and None), this always works
        while curr:
            if curr.next == None:
                seen[curr.next] = None
            if curr.random == None:
                seen[curr.random] = None
            seen[curr].next = seen[curr.next]
            seen[curr].random = seen[curr.random]
            curr = curr.next

        return seen[head]
        #The head of the original list is head.
