class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        curr = 0

        for num in nums:
            curr += num
            maxsum = max(curr, maxsum)
            if curr < 0:
                curr = 0
        return maxsum