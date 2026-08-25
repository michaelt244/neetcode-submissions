class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


    
        queue = deque()
        fresh, time = 0, 0
        
        ROW, COL = len(grid), len(grid[0])
        for r in range (ROW):
            for c in range (COL):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        neightbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        #still have rotten oranges + fresh ones to serach
        while queue and fresh > 0:

            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in neightbors:
                    nr, nc = r + dr, c + dc

                    #checking if its in bound and fresh orange, make rotten
                    if min(nr, nc ) < 0 or nr == ROW or nc == COL or grid[nr][nc] != 1:
                        continue

                    #if there is a rotten fruit as a neighbor add it to the queue will pop after were done with that level
                    grid[nr][nc] = 2
                  
                    queue.append((nr, nc))
                    fresh -= 1
            #new row to check       
            time += 1
        
        if fresh > 0:
            return -1
        return time

    