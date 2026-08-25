class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        color = [0] * 3

        for i in range(len(nums)):
            color[nums[i]] += 1
        
        print(color)

        i = 0
        for j in range(len(color)):
            for k in range(color[j]):
                nums[i] = j
                i += 1
        
        return nums

        