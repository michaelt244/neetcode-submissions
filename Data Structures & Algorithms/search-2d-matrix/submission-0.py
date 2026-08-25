class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows
        # rows = len(matrix)

        # Get the number of columns (length of the first row)
        # cols = len(matrix[0])

        for Row in range(len(matrix)):
            for Col in range(len(matrix[0])):
                if matrix[Row][Col] == target:
                    return True
        return False


        