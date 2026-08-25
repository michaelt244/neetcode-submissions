class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []
        for i, num in enumerate(nums):
            left, right = i + 1 , len(nums) - 1

            while(left < right):
                add = num + nums[left] + nums[right]

                if (add < 0):
                    left += 1
                if (add > 0):
                    right -= 1
                result.append(num, nums[right], nums[left])
                break

        return [result]