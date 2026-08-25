class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        count = 0
        current_sum = 0

        #both start at 0, we are moving the right pointer
        for R in range(len(arr)):
            #keep track of the current sume of vlaues
            current_sum += arr[R]

            #when we noticed that the right ponter is >= k -1 (the window) thats 
            #when we know we have valid window sizes (k) -> R starts at 0
            if R >= k - 1:
                #if currnet avg is greater than threshold increase count
                if current_sum/k >= threshold:
                    count += 1
                #remove the left pointers sum before increaseing it
                current_sum -= arr[L]
                L += 1        
        return count
            
        