class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        look = set(nums)
        count = 0
        for num in nums:
            if num - 1 not in look:
                temp, c = num, 0
                while(temp in look):
                    c += 1
                    temp += 1
                if c > count:
                    count = c
        return count