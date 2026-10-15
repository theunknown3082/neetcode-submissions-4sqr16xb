class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        cols, posDiag, negDiag = set(), set(), set()

        def backtrack(r):
            # base case: end of board:
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            # looping
            for c in range(n):
                if c not in cols and (r + c) not in posDiag and (r - c) not in negDiag:
                    cols.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    board[r][c] = 'Q'
                    
                    backtrack(r + 1)

                    cols.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    board[r][c] = '.'


        backtrack(0)
        return res