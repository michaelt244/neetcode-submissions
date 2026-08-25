class node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #map to key to node

        #left is least recently used 
        self.left = node(0,0)

        #right is recently used
        self.right = node(0,0)

        #conntecting the list together
        self.left.next = self.right
        self.right.prev = self.left

    #remove from the list
    def remove(self, node):
        prev, nxt = node.prev, node.next

        #remove the middle node
        prev.next, nxt.prev = nxt, prev
    
    #insert at right
    def insert(self, node):
        
        prev, nxt = self.right.prev, self.right

        prev.next = nxt.prev = node

        node.next, node.prev = nxt, prev



    def get(self, key: int) -> int:
        #check if key is in the cache 
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val #tells us the vlaue of node
        return -1
    


    def put(self, key: int, value: int) -> None:
        #adding it to the end of the list if space if repalce (head)

        if key in self.cache:
            self.remove(self.cache[key])
        
        #updating the new value of the key + inserting it to the list
        self.cache[key] = node(key, value)
        self.insert(self.cache[key])

        #if capcacity is reached we delete the least visted node (left pointer)
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]




        
