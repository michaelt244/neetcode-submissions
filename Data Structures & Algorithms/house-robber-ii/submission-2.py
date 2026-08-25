class Solution:
    def rob(self, nums: List[int]) -> int:

        #edge case where we only have two numbers or less
        if len(nums) <= 2:
            return max(nums)


        def robbing(nums):
            rob1, rob2 = 0, 0 

            for num in nums:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        #we can just make a generic helper function following the house robber format

        #then since the first and last house are linked we can break it up into two problems one where the first house is not valid and the last house is not valid
        #then we can take the max of those houeses and the bigger one is the awnser
        return max(robbing(nums[1:]), robbing(nums[:-1]))