class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        left = {}
        right = {}

        for c in s:
            if c not in left:
                left[c] = 1
            left[c] += 1
        
        for c in t:
            if c not in right:
                right[c] = 1
            right[c] += 1
        
        return left == right
