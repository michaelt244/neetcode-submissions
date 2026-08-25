class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        code = "#"

        for word in strs:
            encoded_string += str(len(word)) + code + word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while str[j] != '#':
                j += 1       
            length = int(str[i:j])
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        
