class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:


        #keeping track of the largest and smallest subarray
        max_sum = nums[0]
        min_sum = nums[0]


        curr_max_sum = 0
        curr_min_sum = 0

        total = 0
        

        for n in nums:
            
            #if the current max sum ever goes negative reset it to 0
            curr_max_sum = max(curr_max_sum, 0)
            #if the currnent min sum goes postive reset it
            curr_min_sum = min(curr_min_sum, 0)

            #add to the current max sum 
            curr_max_sum += n

            #add to the current min sum
            curr_min_sum += n

            #keeping track of the total sum  
            total += n

            #check if theres a new max sum 
            max_sum = max(max_sum, curr_max_sum)
            min_sum = min(min_sum, curr_min_sum)

        

        #if the max_sum is the largest return it
        if max_sum > total - min_sum:
            return max_sum

        #if the total - min sum is 0 that menas all the values are negative so return the larget number
        elif total - min_sum == 0:
            return max(nums)
        else:
            return total - min_sum
