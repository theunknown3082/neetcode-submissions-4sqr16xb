class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def backtrack(r, c):
            # base case
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return

            # we change it to T
            board[r][c] = "T"
            backtrack(r + 1, c)
            backtrack(r - 1, c)
            backtrack(r, c + 1)
            backtrack(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if (r in [0, rows - 1] or c in [0, cols - 1]) and board[r][c] == "O":
                    backtrack(r, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"