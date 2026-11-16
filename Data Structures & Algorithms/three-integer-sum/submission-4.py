class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        i = 0

        while i < len(nums):
            if nums[i] > 0:
                return res
            if i > 0:
                if nums[i] == nums[i - 1]:
                    i += 1
                    continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            i += 1
                
        return res