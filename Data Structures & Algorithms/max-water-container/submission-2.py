class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx = 0

        left, right = 0, len(heights) - 1
        while(left < right):
            lenght = right - left
            if heights[left] < heights[right]:
                temp = lenght * heights[left]
                if temp > maxx:
                    maxx = temp
                left += 1
            else:
                temp = lenght * heights[right]
                if temp > maxx:
                    maxx = temp
                right -= 1
        
        return maxx
