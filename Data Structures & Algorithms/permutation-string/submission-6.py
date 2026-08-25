from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
    
        L = 0
        s1_counter = Counter(s1)
        window_counter = Counter()
        for R in range(len(s2)):
            
            window_counter[s2[R]] += 1 

            if R - L + 1 > len(s1):
                window_counter[s2[L]] -= 1
                if window_counter[s2[L]] == 0:
                    del window_counter[s2[L]]
                L += 1

            if s1_counter == window_counter:
                return True
        
        return False
            
        