
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        if(self.head.next == self.tail):
            return True
        return False
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail  
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        first_node = self.head.next

        first_node.prev = new_node
        new_node.next = first_node
        new_node.prev = self.head
        self.head.next = new_node
        

    def pop(self) -> int:
        if(self.isEmpty()):
            return -1
        
        last_node = self.tail.prev
        new_last = last_node.prev

        new_last.next = self.tail
        self.tail.prev = new_last

        return last_node.value

    def popleft(self) -> int:
        if(self.isEmpty()):
            return -1
        
        first_node = self.head.next
        new_first = first_node.next

        new_first.prev = self.head
        self.head.next = new_first

        return first_node.value




