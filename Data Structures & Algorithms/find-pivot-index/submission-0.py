class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        sum_list = [0] * len(nums) + 1

        for i in range(len(nums)):
            sum_list[i + 1] = sum_list[i] + nums[i]
        

        for i in range(len(nums)):
            left = 0
            right = len(nums) - 1

            if sum_list[left] == sum_list[right]:
                return i
            
        return -1
        