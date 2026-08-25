class Solution:

    def encode(self, strs: List[str]) -> str:
        decorder = "#"
        ans = ""
        for word in strs:
            ans += str(len(word)) + decorder + word
        return ans
            

    def decode(self, s: str) -> List[str]:
        lister = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            lister.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        
        return lister