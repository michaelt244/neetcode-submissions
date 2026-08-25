class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        l = [1] * len(nums)
       #[1, 1, 1, 1, 1, 1, ... len(nums)]
       
       # start at 1 since there is nothing to the left at the first index
        left = 1

        # get all the multplication values to the left
        for i in range(len(nums)): 
            l[i] = left
            left *= nums[i]

    
        # start at 1 since there is nothing to the right at the last index
        right = 1
        #gel all the multplication values to the right
        for i in range(len(nums) - 1, -1 , -1):
            # times that right value with waht is alreday in the left to get everything 
            # to the right and left of that index
            l[i] *= right
            right *= nums[i]

        return l
