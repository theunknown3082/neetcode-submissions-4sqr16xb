class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []
        n = len(s)

        def backtrack(i):
            if i == n:
                res.append(sol.copy())
                return
            for j in range(i, n):
                if palcheck(i, j):
                    sol.append(s[i : j + 1])
                    backtrack(j + 1)
                    sol.pop()
            

        def palcheck(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        backtrack(0)
        return res