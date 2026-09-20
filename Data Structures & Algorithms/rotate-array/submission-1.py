class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        left, right = k - 1, len(nums) - 1
        while left >= 0:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp

            left -= 1
            right -= 1
        print(nums)

        