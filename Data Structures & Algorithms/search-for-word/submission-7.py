class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


        def tracer(r, c, index):

            if len(word) == index:
                return True

            if r >= ROWS or c >= COLS or min(r, c) < 0:
                return False

            #check if the current r,c is mapped correcntly to the words index if not or the cell has already been visted we can mark it as false
            if board[r][c] != word[index] or board[r][c] == "#":
                return False

            
            #move r, c in the 4 path it can move
            board[r][c] = "x"

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if tracer(nr, nc, index + 1) == True:
                    return True

            board[r][c] = word[index]
            return False
        

        #from each charcter in the matrix try the tracer on it
        for r in range(ROWS):
            for c in range(COLS):
                if tracer(r, c, 0):
                    return True
        
        #the word was not found 
        return False



        