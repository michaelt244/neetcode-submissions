class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        for num in nums:
            #finding the index as list is [1, n] inclusive
            idx = abs(num) - 1

            #if its mapped to a negative number we have already seen
            #this number meaning it is a dupilicate as we mark 
            #numbers negative for the ones we have seen
            if nums[idx] < 0:
                #return the number (abs(number)) since we marked it as seen (-number)
                return abs(num)
            #marking the number as seen (2 -> -2)
            nums[idx] *= -1
        
        #-1 if no duplicate is found
        return -1
         
           