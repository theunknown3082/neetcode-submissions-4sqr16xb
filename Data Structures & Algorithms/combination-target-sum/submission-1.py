class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(i, total):
            # base case 1
            if total == target:
                res.append(sol.copy())
                return
            # base case 2
            if i >= n or total > target:
                return

            # we do not take the current nums[i]
            backtrack(i + 1, total)

            # we take the current nums[i]
            sol.append(nums[i])
            backtrack(i, total + nums[i])
            sol.pop()

        
        backtrack(0, 0)
        return res