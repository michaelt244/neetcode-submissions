class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True


        for i in range(len(s) -1, -1, -1):
            for word in wordDict:

                end = i + len(word)
                #does the word fit and is in the word!
                if (end <= len(s) and s[i: end] == word):
                    dp[i] = dp[i + len(word)]

                if dp[i]:
                    break
            
        
        return dp[0]
