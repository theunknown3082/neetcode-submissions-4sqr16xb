class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        
        def backtrack(i):
            # base case when we reach the end
            if i == n:
                res.append(sol.copy())
                return

            # situation 1 where we dont pick, so we move further
            backtrack(i + 1)

            # now situation 2 where we pick, and then move further by backtracking
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)
        return res