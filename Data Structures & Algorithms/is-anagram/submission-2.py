class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = set()
        word2 = set()

        for i in range(len(s)):
            word1.add(s[i])

        for i in range(len(t)):
            word2.add(t[i])
        
        return word1 == word2
        