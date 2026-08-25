class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #two pointers approach
        left, right = 0, len(heights) - 1

        area_max = 0

        while left < right:
            #lowest side
            height = min(heights[left], heights[right])
            #calculating the area between the two points
            area = height * (right - left)
            
            #if the new area is bigger replace curent max
            if area > area_max:
                area_max = area
            
            #move the smaller height
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -=1
            else:
                right -= 1
                left += 1
            
        return area_max