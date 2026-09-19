class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix = []
        suffix = [0] * len(nums)

        total_prefix = 0
        for n in nums:
            total_prefix += n 
            prefix.append(total_prefix)
        
        total_suffix = 0 
        for i in range(len(nums) - 1, -1, -1):
            total_suffix += nums[i]
            suffix[i] = total_suffix
        
        for i in range(len(nums)):
            if i == 0:
                left = 0
                right = suffix[1] if len(nums) > 1 else 0 
            elif i == len(nums) - 1:
                left = prefix[i - 1]
                right = 0
            else:
                left = prefix[i - 1]
                right = suffix[i + 1]
            
            if left == right:
                return i
        return -1


         