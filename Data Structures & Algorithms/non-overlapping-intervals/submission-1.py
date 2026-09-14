class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

    if not intervals:
      return 0
    intervals.sort(key=lambda x: x[0])

    prevous_end = intervals[0][1]

    remove_count = 0

    for i in range(1, len(intervals)):
      if prevous_end > intervals[i][1]:
        # there is an overlap so get rid of the current one since the ends overlap (the current end is large than the next one)
        remove_count += 1
      prevous_end = min(prevous_end, intervals[i][1])


    return remove_count
