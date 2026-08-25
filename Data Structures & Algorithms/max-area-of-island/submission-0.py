class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        max_area = 0


        def dfs(r, c, count):
            if min(r,c) < 0 or r == ROW or c == COL or grid[r][c] != 1: 
                return count
            
            grid[r][c] = 0

            count = 1 + dfs(r + 1, c, count) +  dfs(r - 1, c, count) + dfs(r, c + 1, count) + dfs(r, c - 1, count)

            return count
        

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c, 0))
        
        return max_area
                


            

        