class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx = 0

        left, right = 0, len(heights) - 1
        while(left < right):
            lenght = right - left
            if heights[left] < heights[right]:
                temp = length * heights[left]
                if temp > maxx:
                    maxx = temp
                left += 1
            else:
                temp = length * heights[right]
                if temp > max:
                    maxx = temp
                right -= 1
        
        return maxx
