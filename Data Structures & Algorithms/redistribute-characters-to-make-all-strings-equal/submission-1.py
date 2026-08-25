from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) < 1:
            return False

        mapper = []

        for i, word in enumerate(words):
            if list(Counter(word)) in mapper:
                return True
            mapper.append(list(Counter(word)))
        return False 