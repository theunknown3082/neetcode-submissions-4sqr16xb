class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, curr, farthest = 0, 0, 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == curr:
                jumps += 1
                curr = farthest

        return jumps