class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = [intervals[0]]
        n = len(intervals)

        for idx in range(1, n):
            if res[-1][1] <= intervals[idx][0]:
                res.append(intervals[idx])
            else:
                res[-1][1] = min(res[-1][1], intervals[idx][1])
        
        return n - len(res)
