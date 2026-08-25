
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #building a hashmap of nums for quick lookup
        sequence = set(nums)
        count = 0
        for num in nums:
            arr = []

            #cant be the start of the sequence since its not the smallest number possible
            #so we skip it
            if num - 1 in nums:
                continue
              
            arr.append(num)
            current_lenght = 1

            while num + 1 in sequence:
                arr.append(num + 1)
                current_lenght += 1
                num += 1
            count = max(current_lenght, count)

        return count

            

            
            
            
            

        