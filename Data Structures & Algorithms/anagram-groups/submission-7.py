from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for i, strr in enumerate(strs):
            if strr in group:
                group[i].append(strr)
            group[i] = strr
        return group




        