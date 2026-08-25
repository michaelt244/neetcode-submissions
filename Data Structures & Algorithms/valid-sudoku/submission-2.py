from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        valid_rows = defaultdict(set) 
        valid_columns = defaultdict(set) 
        valid_sqaure = defaultdict(set) 


        rows = len(board)
        columns = len(board[0])


        for i in range(rows):
            for j in range(columns):
                if board[i][j] != '.':
                    if board[i][j] not in valid_rows[i]:
                        valid_rows[i].add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in valid_columns[j]:
                        valid_columns[j].add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in valid_sqaure[i//3, j//3]:
                        valid_sqaure[i//3, j//3].add(board[i][j])
                    else:
                        return False
            
        return True

