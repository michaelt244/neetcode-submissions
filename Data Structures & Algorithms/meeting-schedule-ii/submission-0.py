"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:


        if not intervals:
            return 0

        #sorting based on start time
        intervals.sort(key=lambda interval: interval.start)

        rooms = [intervals[0].end] # starting with the first meeting
        heapq.heapify(rooms)


        for interval in intervals[1:]:
            #check the first meeting room and if it has expreired is so pop or add

            if rooms[0] <= interval.start:
                heapq.heappop(rooms)
                heapq.heappush(rooms, interval.end)
            else:
                #if not eneded we need to make a new room
                heapq.heappush(rooms, interval.end)


        return len(rooms)

