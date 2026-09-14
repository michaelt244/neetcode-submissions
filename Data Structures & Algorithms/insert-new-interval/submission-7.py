class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]


        output = []

        #start, end

        for i in range(len(intervals)):
            #if the new interval comes before the current invterval add it to the current interval
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]

            #if the new interval comes after the current interval add it after the current interval
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])
            #if the new interval is overlapping fix the currnent postioning
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
        #add the new interval to the output
        output.append(newInterval)

        return output 