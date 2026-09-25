class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs)
        prefix = 0

        while prefix <= len(smallest):
            count = 0 
            for word in strs: 
                if word[prefix] == smallest[prefix]:
                    count += 1

            if count != len(strs):
                break
            prefix += 1
            
                

        return smallest[:prefix] 
        