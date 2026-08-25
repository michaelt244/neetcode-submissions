class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        location = list[0]

        for num in nums:
            compare = num
            if compare == val:
                nums.remove(num)
                location = num
            else:
                location = num
        return location
