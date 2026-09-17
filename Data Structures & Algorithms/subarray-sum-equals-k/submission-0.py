class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        result = 0
        current_sum = 0 
        prefix_sums = {0: 1}

        for value in nums:
            current_sum += value
            diff = current_sum - k

            result += prefix_sums.get(diff, 0)

            prefix_sums[current_sum] = 1 + prefix_sums.get(current_sum, 0)
        
        return result

        