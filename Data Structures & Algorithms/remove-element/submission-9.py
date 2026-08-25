class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = len(nums)
        compare = 0

        while compare < count:
            if nums[compare] == val:
                count = count - 1
                compare = compare + 1
            else:
                compare = compare + 1
        return count 
            

    
