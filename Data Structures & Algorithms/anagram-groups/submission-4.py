from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for i, strr in enumerate(strs):
            if strr.sort() in group:
                group[i] += strr
            group[i] = strr
        
        return group




        