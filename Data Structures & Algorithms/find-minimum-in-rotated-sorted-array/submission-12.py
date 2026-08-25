class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        smallest = nums[left]

        while left <= right:
            middle = (left + right) // 2


            if nums[mid] > nums[right]:
                # The pivot/min is in the right half
                left = mid + 1
            else:
                # The pivot/min is in the left half (including mid)
                right = mid




        return samllest 


        