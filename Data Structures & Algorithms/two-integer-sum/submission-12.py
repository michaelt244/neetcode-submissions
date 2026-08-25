class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        seen =  {}

        for i, num in enumerate(nums):
            #we need to see if two numbers eqaul the traget
            #we can pay pass this by doing num(current num) + ? = target
            #so we just need to see if ? is in the list and if so we have our two numbers
            the_one = target - num
            if the_one in seen:
                return [seen[the_one], i]
            # we map the num - index, since we care about the index
            # we just map all the numbers
            seen[num] = i
        
        return []
