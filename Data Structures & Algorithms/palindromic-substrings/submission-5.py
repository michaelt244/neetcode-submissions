class Solution:
    def countSubstrings(self, s: str) -> int:

        res = []
        count = 0

        if len(s) == 1:
            return 1
        

        for i in range(len(s)):

            #even palindromic words
            l, r = i, i 
            while (0 <= l and r < len(s) and s[l] == s[r] ):
                count += 1 
                l -= 1
                r += 1
            

            #odd palindromic words

            l, r = i, i + 1
            while (0 <= l and r < len(s) and s[l] == s[r] ):
                count +=1
                l -= 1
                r += 1  
        
        #print(res)
        return count
            
        