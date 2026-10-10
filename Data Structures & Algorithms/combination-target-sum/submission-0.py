class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        
        def backtrack(i, total):
            if total == target:
                res.append(sol.copy())
                return
            if i >= n or total > target:
                return
            
            sol.append(nums[i])
            backtrack(i, total + nums[i])
            
            sol.pop()

            backtrack(i + 1, total)

        backtrack(0, 0)
        return res