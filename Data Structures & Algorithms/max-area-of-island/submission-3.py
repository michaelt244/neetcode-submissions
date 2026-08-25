class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        max_area = 0
        

        visit = set()



        def dfs(r, c):
            if min(r,c) < 0 or r == ROW or c == COL or grid[r][c] != 1 or (r, c) in visit: 
                return 0
            
            visit.add((r,c))

            return 1 + dfs(r + 1, c) +  dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)        

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area
                


            

        