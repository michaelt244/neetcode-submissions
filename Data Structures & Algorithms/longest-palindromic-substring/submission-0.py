class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        result = ""
        reslen = 0

        for i in range(len(s)):
            #checking odd length palindromes

            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > reslen:
                    result = s[left: right + 1]
                    reslen = right - left + 1
                
                left -= 1 
                right += 1


            #checking for even length palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > reslen:
                    result = s[left: right + 1]
                    reslen = right - left + 1
                
                right += 1
                left -=1
        
        return result
