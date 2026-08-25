class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows
        # rows = len(matrix)

        # Get the number of columns (length of the first row)
        # cols = len(matrix[0])
        rows, cols = len(matrix), len(matrix[0])


        top, bot = 0, rows - 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        

        L, R = 0, cols - 1
        while L <= R:
            mid = (L + R) // 2

            if target > matrix[row][mid]:
                L = mid + 1
            elif target < matrix[row][mid]:
                R = mid - 1
            else:
                return True
        
        return False

        