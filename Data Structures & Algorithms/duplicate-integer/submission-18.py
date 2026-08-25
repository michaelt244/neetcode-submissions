class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = {}

        for i, num in enumerate(nums):
            if num in seen.values():
                return True
            else:
                seen[i] = num
        
        return False
            

        