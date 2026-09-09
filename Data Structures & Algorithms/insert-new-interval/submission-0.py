class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:


        if not intervals:
            return newInterval

        #add it to the intervals and then sort them in increaseing order

        intervals.append(newInterval)
        intervals.sort(key=lambda interval: interval[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= output[-1][1]:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start,end])
        return output