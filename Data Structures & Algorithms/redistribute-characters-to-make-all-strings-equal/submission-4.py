from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        final_str = ""
        mapping_final = defaultdict(int)
        for i in words:
            final_str += i
        for j in final_str:
            mapping_final[j] += 1
        counts = mapping_final.values()
        n = len(words)
        for k in counts:
            if k % n != 0:
                return False
        return True


