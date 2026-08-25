from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #creating dictionarys for (rows, column, and square checking)
        valid_rows = defaultdict(set) 
        valid_columns = defaultdict(set) 
        valid_sqaure = defaultdict(set) 


        rows = len(board)
        columns = len(board[0])


        for i in range(rows):
            for j in range(columns):
                #skipping empty pieces 
                if board[i][j] == '.':
                    continue 
                #checking if that number is already in that row
                if board[i][j] in valid_rows[i]:
                    return False
                #checking if that number is already in that column
                if board[i][j] in valid_columns[j]:
                    return False
                #checking if that number is already in that square
                #using i//3, j//3 since this bounds each 3x3 as key
                if board[i][j] in valid_sqaure[i//3, j//3]:
                    return False
                
                #aftering checking adding the vlaue in the dictionary
                valid_rows[i].add(board[i][j])
                valid_columns[j].add(board[i][j])
                valid_sqaure[i//3, j//3].add(board[i][j])
        return True

