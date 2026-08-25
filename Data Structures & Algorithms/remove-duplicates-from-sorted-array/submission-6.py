class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left_side = nums[0]
        right_side = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if left_side != right_side:
                left_side = nums[i]
                count = count + 1
            rigth_side[i]
        
        return count

