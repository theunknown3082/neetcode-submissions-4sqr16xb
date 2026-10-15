class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        posDiag, negDiag, col = set(), set(), set()

        def backtrack(r):
            # base case
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c not in col and (r + c) not in posDiag and (r - c) not in negDiag:
                    col.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    board[r][c] = 'Q'

                    backtrack(r + 1)

                    col.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    board[r][c] = '.'

        backtrack(0)
        return res