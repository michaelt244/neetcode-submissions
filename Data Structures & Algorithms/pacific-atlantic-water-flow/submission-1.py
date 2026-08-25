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

                dfs(nr, nc, visited, heights[r][c])
        

        for c in range(COL):
            dfs(0, c, pac, heights[0][c])
            dfs(ROW - 1, c, atl, heights[ROW - 1][c])
        
        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL - 1, atl, heights[r][COL - 1])
        

        result = []

        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])


        return result
