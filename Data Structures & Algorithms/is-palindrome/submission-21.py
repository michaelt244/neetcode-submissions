class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1 

        #using two pointers one from the right and left
        while left < right:
            #looping untill we get a valid letter
            while left < right and not s[left].isalnum():
                left += 1
            #looping untill we get a valid letter
            while left < right and not s[right].isalnum():
                right -=1
            #comparing those two letter
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -=1
        
        return True
        