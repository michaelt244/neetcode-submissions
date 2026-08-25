class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > (n - 1):
            return False
        
        #creating the map for each value
        adj = [[] for _ in range(n)]

        # 0: [1, 2]
        # 1: [0, 3]
        # ... 

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        

        visted = set()

        def dfs(current, parrent):
            #if we already visted it then we have a cycle
            if current in visted:
                return False
            
            #marking the current node as visted
            visted.add(current)

            #now we need to explore its neighbors
            for neighbor in adj[current]:
                #skip if its the parrent (1 -> 0 and 0->1 are okay)
                if neighbor == parrent:
                    continue
                if not dfs(neighbor, current):
                    return False
            
            return True
        

        return dfs(0, -1) and len(visted) == n
        



        