class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Sort array to enable two-pointer technique
        nums.sort()
        ans = []

        # Iterate through each element as potential first number
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            # Two-pointer search for pairs that sum with nums[i] to zero
            while(left < right):

                if nums[i] + nums[left] + nums[right] == 0:
                    #check if the solution is already in the hash map (avoid duplicates)
                    if [nums[i], nums[left], nums[right]] not in ans:
                        ans.append([nums[i], nums[left], nums[right]])
                    #move both pointers
                    right -= 1
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    # Sum too large, need smaller values
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    #sum too small, need larger values
                    left += 1
        return ans