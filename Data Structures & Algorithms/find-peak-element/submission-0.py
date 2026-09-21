class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

        #checking if the left neighbor is greater (search the left side)
        #[1, 2, 3, 2, 5, 6]
        # at 2 since 3 > 2 we need to serach that side since there might be a peak there
        if m > 0 and nums[m] < nums[m - 1]:
            r = m - 1
        
        #checking if the right neighbor is greater (search the right side)
        #[1, 2, 3, 4, 5, 1]
        # at 3 we see that 4 is greater so we need to check the right side since there might be a peak there eventuall also since the end bounday is 0 
        elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
            l = m + 1
        else:
            return m