class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [0] * len(nums)
        prefix = [0] * len(nums)
        surfix = [0] * len(nums)

        # 1 2 3 4 5 
        # 0 0 0 0 0 
        # 1 1 2 6 24 
        # 120 60 20 5 1 

        prefix[0] = 1
        surfix[len(nums) - 1] = 1

        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            surfix[i] = nums[i + 1] * surfix[i + 1]
        for i in range(len(nums)):
            res[i] = prefix[i] * surfix[i]
        
        return res

        