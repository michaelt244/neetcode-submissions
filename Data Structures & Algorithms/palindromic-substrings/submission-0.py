class Solution:
    def countSubstrings(self, s: str) -> int:

        res = []

        if len(s) == 1:
            return [s]
        

        for i in range(len(s)):

            #even palindromic words
            l, r = i, i 
            while (0 <= l and r < len(s) and s[l] == s[r] ):
                res.append(s[l : r])
                l -= 1
                r += 1
            

            #odd palindromic words

            l, r = i, i + 1
            while (0 <= l and r < len(s) and s[l] == s[r] ):
                res.append(s[l : r])
                l -= 1
                r += 1  
        
        print(res)
        return len(res)
            
        