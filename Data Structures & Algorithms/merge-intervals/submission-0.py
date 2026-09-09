class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda interval: interval[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:


            #if its within the latest list add it
            if start <= output[-1][1]:
                output[-1][1] = max(output[-1][1], end)
            
            else:
                output.append([start,end])

        return output