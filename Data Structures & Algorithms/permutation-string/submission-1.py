class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        

        L = 0
        for R in range(len(s2)):
            if R - L + 1 == len(s1):
                if s2[L:R + 1] in s1:
                    return True
                else:
                    L += 1
        return False
            
        