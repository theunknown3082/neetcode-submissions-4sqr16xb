import random
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        while True:
            pick = random.choice(nums)
            if nums.count(pick) > n//2:
                return pick