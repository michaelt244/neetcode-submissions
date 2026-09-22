class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i, j, k):
            
            if k == len(s3):
                #we reach the end of both substrings
                return (i == len(s1) and j == len(s2))
            
            #if we match from s1 move upward
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j , k + 1):
                    return True
            
            #if we match from s2 move upward
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1):
                    return True

            #if current index doesnt match index at s1 or s2 we have no match so return fasle
            return False

        return dfs(0, 0, 0)