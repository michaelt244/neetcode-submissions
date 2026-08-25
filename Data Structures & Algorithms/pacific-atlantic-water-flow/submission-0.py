class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        ROW, COL = len(heights), len(heights[0])

        pac = set()
        atl = set()


        def dfs(r, c, visited, prev):
            if min(r, c) < 0 or r == ROW or c == COL or (r, c) in visited:
                return
            #checking currnet grid[r][c]
            if heights[r][c] < prev:
                return
            visited.add((r, c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            #then moving to the its valid directions
            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if min(nr, nc) < 0 or nr == ROW or nc == COL or (nr, nc) in visited:
                    continue
                dfs(nr, nc, visited, heights[r][c])
            

        # Pacific from top row and left column
        for c in range(COL): dfs(0, c, pac, heights[0][c])
        for r in range(ROW): dfs(r, 0, pac, heights[r][0])

        # Atlantic from bottom row and right column
        for c in range(COL): dfs(ROW-1, c, atl, heights[ROW-1][c])
        for r in range(ROW): dfs(r, COL-1, atl, heights[r][COL-1])
        
        # Intersection
        return [[r,c] for r in range(ROW) for c in range(COL) if (r,c) in pac and (r,c) in atl]
