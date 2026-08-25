class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = nums.sort()
        return len(new_list)
