class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        #left = 0, 
       # right = len(nums) - 1

        ans = [0] * len(nums)

        for i in range(len(nums)):
            left = 0
            right = len(nums) - 1
            l, r = 1, 1
            while left != i:
                l *= nums[left]
                left += 1
            while right != i:
                r *= nums[right]
                right -= 1
            ans[i] = r * l
         #   left = 0
          #  right = len(nums - 1)
        
        return ans
