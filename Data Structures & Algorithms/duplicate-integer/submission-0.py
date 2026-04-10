class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        default = False
        hash = set()
        for i in nums:
            if i in hash:
                default = True
                break
            hash.add(i)
        return default