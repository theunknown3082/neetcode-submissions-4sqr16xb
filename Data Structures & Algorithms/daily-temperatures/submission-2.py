class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for currIdx, currTemp in enumerate(temperatures):
            while stack and currTemp > temperatures[stack[-1]]:
                prevIdx = stack.pop()
                res[prevIdx] = currIdx - prevIdx

            stack.append(currIdx)

        return res 