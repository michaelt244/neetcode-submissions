class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        l = [1] * len(nums)
        left = 1

        for i in range(len(nums)): 
            l[i] = left
            left *= nums[i]

     
        right = 1
        for i in range(len(nums) - 1, -1 , -1):
            l[i] *= right
            right *= nums[i]

        return l
