class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        hay = len(haystack)
        search = len(needle)

        for i in range(hay - search + 1):
            if haystack[i: i + search] == needle:
                return i 
        
        return -1 