class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = {}

        for num, i in enumerate(nums):
            if num in seen:
                return False
            else:
                seen[i] = num
        return False
            

        