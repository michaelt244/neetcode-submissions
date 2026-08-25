"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        new_adjList = {}


        def dfs(node):
            #when there is no more neighbors return 
            #or we already visted this node break it
     
            if node in new_adjList:
                return new_adjList[node]

            #creating the copy
            copy = Node(node.val)
            #storing it in the hashmap
            new_adjList[node] = copy
            
            #calling dfs on the current nodes neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            #return the copy we made
            return copy

        return dfs(node) if node else None