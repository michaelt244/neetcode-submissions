class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = {}

        for num, i in enumerate(nums):
            if num not in seen:
                seen[i] = num
            else:
                return True
                
        return False
            

        