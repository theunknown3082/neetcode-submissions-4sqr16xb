class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        maxreach = 0
        for i in range(len(nums) - 1):
            if i > maxreach:
                return False
            else:
                maxreach = max(maxreach, i + nums[i])

        return True if maxreach >= (len(nums) - 1) else False
