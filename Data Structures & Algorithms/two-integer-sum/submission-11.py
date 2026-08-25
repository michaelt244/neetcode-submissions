class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        seen =  {}

        for i, num in enumerate(nums):
            the_one = target - num
            if the_one in seen:
                return [seen[the_one], i]

            seen[num] = i
        
        return []
