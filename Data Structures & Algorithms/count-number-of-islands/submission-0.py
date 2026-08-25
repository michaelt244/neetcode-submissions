class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        islands = 0


        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == '0': #base case to stop when we see water?
                return
           
            grid[r][c] = '0' #marking it as seen so we do not double count

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return 1
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    if dfs(r, c) == 1:
                        islands += 1
        
        return islands
            



        