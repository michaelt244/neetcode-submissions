class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])

        if ROW == 1 or COL == 1:
            return -1

        if grid[0][0] == 1 or grid[ROW - 1][COL - 1] == 1:
            return -1

        length = 1
        queue = deque()
        visit = set()

        queue.append((0,0))
        visit.add((0, 0))

        def bfs(grid, length):
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    if r == ROW - 1 and c == COL - 1:
                        return length

                    #edge cases handling
                    neightbors = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

                    for right, left in neightbors:
                        nr, nc = r + right, c + left

                        if min(nr, nc) < 0 or nr == ROW or nc == COL or (nr, nc) in visit or grid[nr][nc] != 0:
                            continue #if we hit any of the edge cases then skip to the next valid direction
                        
                        queue.append((nr, nc))
                        visit.add((nr, nc))
                length += 1
        
            return - 1

        return bfs(grid, length)

                

                    



