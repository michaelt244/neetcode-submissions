class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums[0]
        

        bucket = [0] * nums[-1]
        for num in nums:
            bucket[num - 1] += 1
        

        result = bucket[-k:]

