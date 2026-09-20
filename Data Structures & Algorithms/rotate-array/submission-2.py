class Solution:

    def reveser(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)

        if length == 0:
            return

        k = k % length

        #reverse the first n - k elements
        self.reveser(nums, 0, length - k - 1)

        #reverse the rest of the elements
        self.reveser(nums, length - k, length - 1)

        #reverse the entire array
        self.reveser(nums, 0, length - 1)