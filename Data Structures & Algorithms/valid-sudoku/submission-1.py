class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        valid = {}
        rows = len(matrix)
        columns = len(matrix[0])


        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] not in valid[i][j]:
                    valid[i][j].append(matrix[i[j]])
                else:
                    return False
        
        return True

