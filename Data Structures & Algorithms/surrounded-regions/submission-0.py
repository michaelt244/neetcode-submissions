class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def capture(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS:
                return 
            if board[r][c] != "O":
                return 
            
            board[r][c] = "T"

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                capture(nr, nc)

        # capturing the unsurronudede regions

        for r in range(ROWS):
            for c in range(COLS):
                #edge values
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r,c)

        # capturing the surronudede regions

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # uncapture the unsurronudede regions

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"