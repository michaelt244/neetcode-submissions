class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs, key=len)
        prefix = 0

        while prefix <= len(smallest) - 1:
            for word in strs: 
                if word[prefix] != smallest[prefix]:
                    return smallest[:prefix]
            prefix += 1

        return smallest[:prefix] 
        