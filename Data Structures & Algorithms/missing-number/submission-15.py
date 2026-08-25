class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        seen = set(nums)

        for i in range(0, len(nums)):
            if i not in seen:
                return num[i]
        return 0