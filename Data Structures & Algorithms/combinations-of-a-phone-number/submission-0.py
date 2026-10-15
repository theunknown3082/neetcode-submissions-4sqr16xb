class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # main base case: not digits i.e. empty:
        if not digits:
            return []
        
        res, sol = [], []
        n = len(digits)
        digitsToChar = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        def backtrack(i):
            
            # base case: we have took all the digits:
            if i == n:
                res.append("".join(sol))
                return

            # we perform the permutations:
            for x in digitsToChar[digits[i]]:
                sol.append(x)
                backtrack(i + 1)
                sol.pop()

        backtrack(0)
        return res

