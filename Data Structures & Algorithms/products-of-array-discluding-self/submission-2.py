class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        l = [1] * len(nums)
        left = 1

        for i in range(len(nums)): 
            l[i] = left
            left *= nums[i]

     
        r = [1] * len(nums)
        for i in range(len(nums) - 1, 0 , -1):
            r[i] = right
            right *= nums[i]

        return r
