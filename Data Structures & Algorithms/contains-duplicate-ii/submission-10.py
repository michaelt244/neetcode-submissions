class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set()
        left = 0 


        for right in range(len(nums)):
            if right - left + 1 > k:
                window.remove(nums[left])
            if right in window:
                return True
            window.add(nums[left])
        
        return False
        