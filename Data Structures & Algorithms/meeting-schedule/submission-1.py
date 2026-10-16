"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)
        n = len(intervals)
        idx = 1
        while idx < n:
            if intervals[idx].start < intervals[idx - 1].end:
                return False
            idx += 1
        return True
            