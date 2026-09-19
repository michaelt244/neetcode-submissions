
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #building a hashmap of nums for quick lookup
        sequence = set(nums)
        count = 0
        for num in nums:
            arr = []

            # if the current num - 1 is in the list then we know the current num can not be the start
            # of a sequence so we can skip this number
            if num - 1 in sequence:
                continue
            
            #adding current num the current sequence
            arr.append(num)
            current_lenght = 1

            #adding to the current sqsequence is num + 1 is in the list
            while num + 1 in sequence:
                arr.append(num + 1)
                current_lenght += 1
                num += 1
            #checking if the current sequence is the biggest one we have seen so far
            count = max(current_lenght, count)

        #returning the largest sequence we saw
        return count

            

            
            
            
            

        