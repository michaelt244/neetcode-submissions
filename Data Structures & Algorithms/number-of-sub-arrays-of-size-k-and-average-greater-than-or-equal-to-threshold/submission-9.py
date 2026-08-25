class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        currnetsum = 0
        L = 0


        for R in range(len(arr)):
            currnetsum += arr[R]
            if R - L > k:
                currnetsum = 0
                L += 1
            
            if (currnetsum /k) >= threshold:
                count += 1
        
        return count