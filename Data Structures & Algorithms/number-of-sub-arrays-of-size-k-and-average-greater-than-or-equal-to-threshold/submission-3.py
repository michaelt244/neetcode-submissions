class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        window = set()
        L = 0


        for R in range(len(arr)):
            if R - L  + 1 > k:
                window.remove(arr[L])
                L += 1
            avg = sum(window) / k
            if avg >= threshold:
                count += 1
            window.add(arr[R])
        
        return count