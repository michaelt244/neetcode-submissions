class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = 0
        #greatest length
        greatest = 0 


        for R in range(len(s)):
            #remove for the window untill there are no duplicates
            while s[R] in window:
                window.remove(s[L])
                L += 1
            #as we add more charcters, check is the greatest length has increased 
            window.add(s[R])
            greatest = max(len(window), greatest)
        
        #return greatest length we found
        return greatest

        