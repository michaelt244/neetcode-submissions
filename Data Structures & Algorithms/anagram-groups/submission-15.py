from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs:
            check = [0] * 26
            for c in word:
                check[ord(c) - ord('a')] += 1
            
            group[tuple(check)].append(word)
        return list(group.values())




        