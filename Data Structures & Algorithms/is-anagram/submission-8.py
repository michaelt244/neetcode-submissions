from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = []
        word2 = []

        for c in s:
            word1.append(c)
        for c in t:
            word2.append(c)

        print(word1)
        print(word2)
        return word1.sort() != word2.sort()
        