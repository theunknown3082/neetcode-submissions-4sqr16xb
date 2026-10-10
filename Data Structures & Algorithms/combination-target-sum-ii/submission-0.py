class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res, sol = [], []

        def backtrack(i, total):
            if total == target:
                res.append(sol.copy())
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if total + candidates[j] > target: 
                    break
            # we choose the num[i]
                sol.append(candidates[j])
                backtrack(j + 1, total + candidates[j])
                sol.pop()

            

        backtrack(0, 0)
        return res