from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #if s1 is greater than s2 there is no way s1 is a permutation of ss2
        if len(s1) > len(s2):
            return False
        
    
        L = 0

        #a counter of the frequecny of the chracters in s1
        s1_counter = Counter(s1)

        #a counter of the frequecny of the chracters in the window 
        window_counter = Counter()
        for R in range(len(s2)):

            #adding to the window frequecny table (needed since bc = cb ...)
            window_counter[s2[R]] += 1 

            #if the window is big remove from the frequecny table 
            if R - L + 1 > len(s1):
                #decrease count and remove it the count goes to 0
                window_counter[s2[L]] -= 1
                if window_counter[s2[L]] == 0:
                    del window_counter[s2[L]]
                #move the left pointer
                L += 1

            #if the counters match then s1 is permutation of s2
            if s1_counter == window_counter:
                return True
        
        #return false if s1 is not a permutation of s2
        return False
            
        