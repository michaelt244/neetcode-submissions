class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        final_str = ""
        final_map = defaultdict(int)

        for word in words:
            final_str += word
        
        for c in final_str:
            final_map[c] += 1
        
        length = len(words)

        for j in final_map:
            if final_map[j] % length != 0:
                return False
        
        return True


            