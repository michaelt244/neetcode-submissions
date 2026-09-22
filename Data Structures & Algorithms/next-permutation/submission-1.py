class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1
        dip = -1
        #finding the first dip in the list
        while right  > 0:
            if nums[right] > nums[right - 1]:
                dip = right - 1
                break
            right -= 1
        
        #if not dip means were at the greatest permutation so just reverse the list
        if dip == -1:
            nums.reverse()
            return

        #finding the rightmost greatest value
        right = len(nums) - 1
        while right > dip:
            if nums[right] > nums[dip]:
                nums[dip], nums[right] = nums[right], nums[dip]
                break
            right -= 1
        
        nums[dip + 1:] = reversed(nums[dip + 1:])