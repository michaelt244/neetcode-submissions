class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        seen = set(nums)
        return count(seen)
        