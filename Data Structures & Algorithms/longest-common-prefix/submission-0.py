class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        strs = sorted(strs)
        for index in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][index] != strs[-1][index]:
                return strs[0][:index]
        return strs[0]