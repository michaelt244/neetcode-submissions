class Solution:

    def encode(self, strs: List[str]) -> str:
        decorder = "#"
        ans = ""

        # we need to find a place to keep track of all the words were using a decorder(#)
        # to help us know when we have a new word but also the length of the worder since
        # "#" can also be a charcter 
        for word in strs:
            ans += str(len(word)) + decorder + word
        return ans
            

    def decode(self, s: str) -> List[str]:
        lister = []
        i = 0

        # loop throught the lenght of the string s
        while i < len(s):
            j = i
            # going up untill we reach our decoder
            while s[j] != "#":
                j += 1
            # the length of the string
            length = int(s[i:j])
            # appned the word
            lister.append(s[j + 1 : j + 1 + length])
            #update i to loop again and find the next decorder to help us find the next wword
            i = j + 1 + length
        
        return lister