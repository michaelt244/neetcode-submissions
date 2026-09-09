"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        window = []

        if not intervals:
            return True

        intervals.sort(key=lambda interval : interval.start)

        window = intervals[0]

        for interval in intervals[1:]:
            if interval.start <= window.end:
                window.end = max(window.end, interval.end)
                return False
            else:
                window = interval      

        return True

        
