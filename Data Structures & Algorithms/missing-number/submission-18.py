class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        seen = set(nums)

        for i in range(0, len(nums)):
            if nums[i] not in seen:
                return nums[i]