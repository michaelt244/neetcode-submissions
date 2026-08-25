class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        look = set(nums)
        count = 0
        for i, num in enumerate(nums):
            if num - 1 in look:
                temp = 0
                while(i < len(nums)):
                    if(nums[i + 1] in look):
                        temp += 1
                    i += 1
            if(temp > count):
                count = temp

        