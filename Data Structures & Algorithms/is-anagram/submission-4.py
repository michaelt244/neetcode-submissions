class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}
        word2 = {}

        for c in s:
            word1[c] = c
        for c in t:
            word2[t] = c
        print(word1)
        print(word2)
        return word1 == word2
        