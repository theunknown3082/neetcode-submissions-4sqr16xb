class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1, 1

        for num in nums:
            tempmax = num * curmax

            curmax = max(num, tempmax, num * curmin)
            curmin = min(num, tempmax, num * curmin)

            res = max(res, curmax)

        return res