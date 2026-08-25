class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        count = 0
        current_sum = 0

        for R in range(len(arr)):
            current_sum += arr[R]
            if R >= k - 1:
                if current_sum/k >= threshold:
                    count += 1
                current_sum -= arr[L]
                L += 1        
        return count
            
        