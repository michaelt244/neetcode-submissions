class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

    if not intervals:
      return 0
    intervals.sort(key=lambda x: x[0])

    # we use the end of the interval to track if an overlap is happnining
    prevous_end = intervals[0][1]

    remove_count = 0

    for i in range(1, len(intervals)):
      if prevous_end > intervals[i][0]:
        # if there is overlap count it
        remove_count += 1

        # pick the smallest intervall to keep since the largest one is likely to have more overlaps
      prevous_end = min(prevous_end, intervals[i][1])

    return remove_count
