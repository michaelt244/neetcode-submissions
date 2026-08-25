class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []
        for i, num in enumerate(nums):
            left, right = i + 1 , len(nums) - 1

            if i > 0 and num == nums[i - 1]:
                continue

            while(left < right):
                add = num + nums[left] + nums[right]

                if add == 0:
                    result.append([num, nums[right], nums[left]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif add < 0:
                    left += 1
                elif add > 0:
                    right -= 1

        return result