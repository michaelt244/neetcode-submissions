class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return 0 

        #creating the current max sum (first number) and curr sum
        max_sum = nums[0]
        curr_sum = 0


        for n in nums:

            #if we get to a point where our current sum is negative restart the window
            curr_sum = max(curr_sum, 0)

            #add the current number to the sum
            curr_sum += n 

            #if the current sum is greater than the previous update max sum
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
