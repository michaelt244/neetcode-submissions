class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        samllest = nums[left]

        while left < right:
            middle = (left + right) // 2
            ##samllest = min(samllest, nums[middle])

            if nums[left] < nums[middle]:
                left = middle + 1
                #left side is sorted
            else:
                #rightside is unsorted
                samllest = min(samllest, nums[middle])

                right = middle        

        return samllest 


        