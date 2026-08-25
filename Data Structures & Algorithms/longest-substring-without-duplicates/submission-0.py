class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = 0
        greatest = 0 


        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            print(greatest)
            print(len(window))
            if greatest < len(window):
                greatest = len(window)
        
        return greatest

        