class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        look = set(nums)
        count = 1
        for i, num in enumerate(nums):
            if num - 1 in look:
                temp = 0
                while(i < len(nums)):
                    if(nums[i] + 1 in look):
                        temp += 1
                        if(temp > count):
                            count = temp
                    i += 1

        return count