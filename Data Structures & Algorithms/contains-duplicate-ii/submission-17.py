class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        #using a set to capture the current window size
        window = set()
        left = 0 

        for right in range(len(nums)):
            #if we reach the window limit we increase left + 1 
            #so we can start a new window + remove the left most
            #valu -----  [1,3,5,4] -> old-[1,3,5,] -> new[3,5,4]
            if right - left > k:
                window.remove(nums[left])
                left += 1
            #if its in the window we have a duplicate
            if nums[right] in window:
                return True
            #adding to our window
            window.add(nums[right])
        
        return False
        