class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []
        for i, num in enumerate(nums):
            left, right = i + 1 , len(nums) - 1

            while(left < right):
                add = num + nums[left] + nums[right]

                if (add < target):
                    left += 1
                if (add > target):
                    right -= 1
                result.append([i, right, left])
                break

        return [result]