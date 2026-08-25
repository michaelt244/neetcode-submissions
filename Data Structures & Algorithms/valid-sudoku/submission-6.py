from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        valid_rows = defaultdict(set) 
        valid_columns = defaultdict(set) 
        valid_sqaure = defaultdict(set) 


        rows = 9
        columns = 9


        for i in range(rows):
            for j in range(columns):
                if board[i][j] == '.':
                    continue 
                if board[i][j] in valid_rows[i]:
                    return False
                if board[i][j] in valid_columns[j]:
                    return False
                if board[i][j] in valid_sqaure[i//3, j//3]:
                    return False
                valid_rows[i].add(board[i][j])
                valid_columns[j].add(board[i][j])
                valid_sqaure[i//3, j//3].add(board[i][j])
        return True

