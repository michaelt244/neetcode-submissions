class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])

        prevous_end = intervals[0][1]

        window = []
        window.append(intervals[0])


        for i in range(1, len(intervals)):
            if prevous_end < intervals[i][1]:
                #there is an overlap so get rid of the current one
                continue
            prevous_end = min(prevous_end, intervals[i][1])
            window.append(intervals[i])
        

        print(window)

        return len(window)

     
