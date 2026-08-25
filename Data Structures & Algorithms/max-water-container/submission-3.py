class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx = 0

        left, right = 0, len(heights) - 1
        while(left < right):
            length = right - left
            area = length * min(heights[left], heights[right])
            maxx = max(area, maxx)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxx
