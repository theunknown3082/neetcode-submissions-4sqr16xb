class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []
        
        def backtrack(Lcount, Rcount):
            # base case: we have n number of complete braces
            if n == Lcount == Rcount:
                res.append("".join(sol))
                return
            
            # we put a left brace:
            if Lcount < n:
                sol.append('(')
                backtrack(Lcount + 1, Rcount)
                sol.pop()

            # we put a right brace only if it makes complete braces
            if Rcount < Lcount:
                sol.append(')')
                backtrack(Lcount, Rcount + 1)
                sol.pop()

        backtrack(0, 0)
        return res