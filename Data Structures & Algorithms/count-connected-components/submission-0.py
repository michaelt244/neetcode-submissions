class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        adj = [[] for _ in range(n)]

        #creating the map for each value
        # 0: [1, 2]
        # 1: [0, 3]
        # ... 

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        connections = 0
        visted = set()

        def dfs(root):
            
            if root in visted:
                return #already saw it so skip it
            
            #has not been seen so add it to the list
            visted.add(root)
            for neighbors in adj[root]:
                dfs(neighbors)


        for i in range(n):
            if i not in visted:
                connections += 1
                dfs(i)
        

        return connections


        