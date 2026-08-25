class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while(left < right):
                if nums[i] + nums[left] + nums[right] == 0:
                    if [nums[i], nums[left], nums[right]] not in ans:
                        ans.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
        return ans