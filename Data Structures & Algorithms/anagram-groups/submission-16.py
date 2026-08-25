class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        
        groups = {}
        for word in strs:
            check = [0] * 26

            for w in word:
                check[ord(w) - ord('a')] += 1

            if tuple(check) not in groups:
                groups[tuple(check)] = [word]
            else:
                groups[tuple(check)] += [word]
            
        
        return list(groups.values())
            
            




