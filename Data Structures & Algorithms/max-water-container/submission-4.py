class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0

        right = len(heights) - 1 
        max = 0

        while left < right:
            hight = min(heights[left], heights[right])
            area = hight * (right - left)
            
            if area > max:
                max = area
            
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -=1
            else:
                right -= 1
                left += 1
            
        return max