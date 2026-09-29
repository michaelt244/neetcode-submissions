class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        allowed = set(allowed)

        result = len(words) 
        for word in words:
            for char in word:
                if char not in allowed:
                    result -= 1
                    break
        
        return result
        