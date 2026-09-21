class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if ((m - 1 < 0 or nums[m - 1] != nums[m]) and 
                (m + 1 == len(nums) or nums[m + 1] != nums[m])):
                return nums[m]
            
            #getting the size of the left side
            leftsize = m - 1 if nums[m - 1] == nums[m] else m

            #if the leftside is ddd the missing number is on that side if not its on the right side
            if leftsize % 2 == 1:
                r = m - 1
            else:
                l = m + 1
        