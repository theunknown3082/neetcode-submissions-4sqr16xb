class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []


        def backtrack(n, Lcount, Rcount):
            if Lcount == Rcount == n:
                res.append("".join(sol))
                return

            if Lcount < n:
                sol.append('(')
                backtrack(n, Lcount + 1, Rcount)
                sol.pop()
            
            if Rcount < Lcount:
                sol.append(')')
                backtrack(n, Lcount, Rcount + 1)
                sol.pop()
        
        backtrack(n, 0, 0)
        return res