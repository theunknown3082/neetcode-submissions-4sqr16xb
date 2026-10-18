class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob(houses):
            n = len(houses)
            if n == 1:
                return houses[0]

            dp = [0] * (n + 1)
            
            dp[1] = houses[0]
            dp[2] = max(houses[1], houses[0])

            for i in range(3, n + 1):
                dp[i] = max(dp[i -1], dp[i - 2] + houses[i - 1])

            return dp[n]
        
        return max(rob(nums[:-1]), rob(nums[1:]))
        