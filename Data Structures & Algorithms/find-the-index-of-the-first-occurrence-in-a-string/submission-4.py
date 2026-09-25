class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) == len(needle):
            return 0 if haystack == needle else -1

        left, right = 0, len(needle)

        while right <= len(haystack):
            if haystack[left:right] == needle:
                print(haystack[left:right])
                return left
            
            left += 1
            right += 1
        
        return -1