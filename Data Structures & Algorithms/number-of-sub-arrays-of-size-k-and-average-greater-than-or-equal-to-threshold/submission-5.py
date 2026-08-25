class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        currnetsum = 0
        L = 0


        for R in range(len(arr)):
            if R - L > k:
                currnetsum = 0
                L += 1
            
            if currentsum/k >= threshold:
                count += 1
            currentsum += arr[R]
        
        return count