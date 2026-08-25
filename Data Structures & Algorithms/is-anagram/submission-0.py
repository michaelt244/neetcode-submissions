class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        right = len(str) - 1
        left = str[0]

        while left < right:
            if str[left] != [right]:
                return False
            left += 1
            right -1
        return True
        