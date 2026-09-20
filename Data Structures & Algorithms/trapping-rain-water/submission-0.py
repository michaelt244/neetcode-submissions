class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        total = 0 

        #formla for water at heigh[i] = min(maxLeft, maxRight) - height[i]
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                total += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                total += maxRight - height[right]
        
        return total