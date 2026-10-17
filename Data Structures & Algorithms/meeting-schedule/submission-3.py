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
        

        for idx in range(n - 1):
            if intervals[idx].end > intervals[idx + 1].start:
                return False
        return True