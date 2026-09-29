class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        valid = 0 
        for word in words:
            count = Counter(word) 
            total = 0
            for a in allowed:
                total += count[a]
            
            if total == len(word):
                valid += 1
        

        return valid
        