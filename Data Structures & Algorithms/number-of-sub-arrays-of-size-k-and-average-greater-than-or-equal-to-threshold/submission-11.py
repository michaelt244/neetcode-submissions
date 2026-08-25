class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        current = sum(arr[:k-1])


        for R in range(len(arr) - k + 1):
            current += arr[R + k - 1]
            if (current / k) >= threshold:
                count += 1
            current -= arr[R]
        return count