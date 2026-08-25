class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set()
        left = 0 

        if k == 0:
            return False


        for right in range(len(nums)):
            if right - left + 1 > k:
                window.remove(nums[left])
            if nums[right] in window:
                return False
            window.add(nums[right])
        
        return True
        