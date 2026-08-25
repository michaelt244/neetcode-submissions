class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []
        for i, num in enumerate(nums):
            left, right = i + 1 , len(nums) - 1

            while(left < right):
                sum = target + num[left] + num[right]

                if (sum < target):
                    left += 1
                if (sum > target):
                    right -= 1
                result.append([i, right, left])
                break

        return [result]