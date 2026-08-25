class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        ROW, COL = len(grid), len(grid[0])
    
        queue = deque()
        fresh = 0

        for r in range (ROW):
            for c in range (COL):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        def bfs(grid, fresh, total_time): 
            while queue and fresh > 0:
                for i in range(len(queue)):
                    r, c = queue.popleft()
    
                    neightbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                    for right, left in neightbors:
                        nr, nc = r + right, c + left

                        if min(nr, nc ) < 0 or nr == ROW or nc == COL or grid[nr][nc] == 0:
                            continue

                        #if there is a rotten fruit as a neighbor add it to the queue will pop after were done with that level
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -= 1
                            queue.append((nr, nc))
                total_time += 1
            if fresh > 0:
                return - 1

            return total_time

        return bfs(grid, fresh, 0)
    