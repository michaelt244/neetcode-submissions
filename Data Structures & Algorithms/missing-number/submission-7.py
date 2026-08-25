class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        seen = set(nums)

        for i in range(0, len(nums) - 1):
            if n not in seen:
                return n

