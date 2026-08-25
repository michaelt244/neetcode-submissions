from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for i, str in enumerate(strs):
            if Counter(str.sort()) in group:
                group[i] += str
            group[i] = str
        
        return group




        