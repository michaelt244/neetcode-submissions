class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s
        
        longest_palindrome = ""
        longest_len = 0

        for i in range(len(s)):

            #for odd palindromic, treat i as the center and expand outwards at the time

            l, r = i, i 

            while (0 <= l and r < len(s) and s[l] == s[r] ):
                l -= 1
                r += 1
            odd_attempt_len = len(s[l:r])
            odd_attempt = s[l:r] 

            #for even Palindromic, treat i and i + 1 as the center so "bb" as the center
            l, r = i, i + 1
            while (0 <= l and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            even_attempt_len = len(s[l:r])
            even_attempt = s[l:r] 

            if even_attempt_len > longest_len:
                longest_palindrome = even_attempt
            elif odd_attempt_len > longest_len:
                longest_palindrome = odd_attempt
        
        return longest_palindrome