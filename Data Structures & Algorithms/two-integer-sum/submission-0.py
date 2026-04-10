class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # diff = target - nums[i]
        hash = {}

        for index, item in enumerate(nums):
            diff = target - item
            if diff in hash:
                return [hash[diff], index]
            hash[item] = index
