class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        orignal_color = image[sr][sc]
        if orignal_color == color:
            return image
        
        ROW, COLUMN = len(image), len(image[0])

        def dfs(r, c):
            if min(r,c) < 0 or r == ROW or c == COLUMN or image[r][c] != orignal_color:
                return
            
            if image[r][c] == orignal_color:
                image[r][c] = color
    
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)
        return image
        