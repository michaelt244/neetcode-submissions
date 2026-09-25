class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left, right = 0, len(needle)

        print(needle[left:right])

        
        while right <= len(haystack) - 1:
            if haystack[left:right] == needle:
                print(haystack[left:right])
                return left
            
            left += 1
            right += 1
        
        return -1