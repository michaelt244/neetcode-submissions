class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        left = {}
        right = {}

        for i in range(len(t)):

            left[t[i]] = left.get(t[i], 0) + 1
            right[s[i]] = right.get(s[i], 0) + 1
        

        print(left)
        print(right)
        
        return left == right
