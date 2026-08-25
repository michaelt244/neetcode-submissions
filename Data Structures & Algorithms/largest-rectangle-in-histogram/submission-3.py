class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stacker = [0]
        for i, heigh in enumerate(heights):
            l, r = i, i
            
            while l - 1 >= 0 and heights[l-1] >= heigh:
                l -= 1
            while r + 1 < len(heights) and heights[r + 1] >= heigh:
                r += 1
            
            width= r - l + 1
            area = heigh * width

            if stacker[-1] < area:
                stacker.append(area)
            
        return stacker.pop()
            
                
            