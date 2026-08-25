class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        samllest = nums[left]

        while left < right:
            middle = (left + right) // 2
            ##samllest = min(samllest, nums[middle])

            if nums[left] < nums[middle]:
                left = middle + 1

            else:
                right = middle - 1
                samllest = min(samllest, nums[middle])
        

        return samllest 


        