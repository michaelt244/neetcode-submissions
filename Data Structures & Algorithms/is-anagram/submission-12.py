from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = []
        word2 = []

        for c in s:
            word1.append(c)
        for c in t:
            word2.append(c)

        word1.sort()
        word2.sort()
        Counter1 = Counter(word1)
        Counter2 = Counter(word2)
        return Counter1 == Counter2
        