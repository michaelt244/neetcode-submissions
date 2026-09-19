class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0

        for n in nums:
            total += n
            self.prefix.append(total)

        

    def sumRange(self, left: int, right: int) -> int:
        # [2, 5, 10, 20, 3] - nums
        # [2, 7, 17, 37, 40] - prefix
        #  0. 1.  2. 3.  4. 
        # (1, 3) = 5 + 10 + 20 = 35
        # prefix[3] = 37 - prefix [0] = 35
        # so its prefix[right] - prefix[left - 1]
        # (2, 3) = 30 -> prefix[3] = 37 - prfeix[1] = 7 = 30 
        # trick is the sum between left, right is just prefix[right] - prefix[left]
        # if left == 0  just then its the prefix[right]

        if left == 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left - 1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)