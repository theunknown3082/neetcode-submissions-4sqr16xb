class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        res = []
        n = len(intervals)
        idx = 0

        while idx < n and intervals[idx][1] < newInterval[0]:
            res.append(intervals[idx])
            idx += 1

        minStart, maxEnd = newInterval[0], newInterval[1]

        while idx < n and intervals[idx][0] <= newInterval[1]:
            minStart = min(minStart, intervals[idx][0])
            maxEnd = max(maxEnd, intervals[idx][1])
            idx += 1
        res.append([minStart, maxEnd])

        while idx < n:
            res.append(intervals[idx])
            idx += 1
        return res
