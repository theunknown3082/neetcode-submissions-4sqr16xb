class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, total):
            # base case, we found target:
            if total == target:
                res.append(sol.copy())
                return

            # base case, we ran out of index or did not find:
            if total > target or i == n:
                return
            # we take:
            sol.append(candidates[i])
            backtrack(i + 1, total + candidates[i])
            sol.pop()

            # we dont take while taking care of reps:
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, total)

        backtrack(0, 0)
        return res
