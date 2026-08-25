class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROW, COL = len(grid), len(grid[0])  

        #land 
        INF = 2^31 - 1

        queue = deque()

        #doing bfs starting at each chest location 
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r,c))

        neightbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        #finding the cloest land location
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in neightbors:
                    nr, nc = r + dr, c + dc

                    if min(nr,nc) < 0 or nr == ROW or nc == COL or grid[nr][nc] == -1:
                        continue #skipping invalid locations
                    if grid[nr][nc] == 2147483647:
                        grid[nr][nc] = grid[r][c] + 1

                        queue.append((nr, nc))
                    
                    
                    

                

            

        


                          

