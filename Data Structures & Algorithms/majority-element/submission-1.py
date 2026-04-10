class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res, maxcount =0, 0
        for num in nums:
            count[num] += 1
            if count[num] > maxcount:
                res = num
                maxcount = count[num]
        return res