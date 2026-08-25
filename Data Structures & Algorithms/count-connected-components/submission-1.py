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
        visited = set()

        def dfs(root):
            
            if root in visited:
                return #already saw it so skip it
            
            #has not been seen so add it to the list
            visited.add(root)
            for neighbors in adj[root]:
                dfs(neighbors)


        for n in range(n):
            if n not in visited:
                connections += 1
                dfs(n)
        

        return connections


        