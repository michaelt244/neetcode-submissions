from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
    
        L = 0
        list1 = Counter(s1)
        for R in range(len(s2)):
            if R - L + 1 == len(s1):
                if list1 == Counter(s2[L:R + 1]):
                    return True
                else:
                    L += 1
        return False
            
        