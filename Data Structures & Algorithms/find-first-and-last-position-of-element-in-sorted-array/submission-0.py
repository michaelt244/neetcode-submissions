class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        smallest, biggest = -1, -1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                smallest = m
                r = m - 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        

        l, r = 0, len(nums) - 1 
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                biggest = m
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        

        return [smallest, biggest]