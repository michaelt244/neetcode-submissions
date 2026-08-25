class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        path = []
        candidates.sort()

        def dfs(i, cur, total):
            #base case to append to the result
            if total == target:
                result.append(cur.copy())
                return
            
            #base case when we turn (total is too big)
            if i == len(candidates) or total > target:
                return
            
            #include the candidates at index i
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            #pop so we can move on to the next step
            cur.pop()

            #skip candidate at index i
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                #move it the last duplicate location
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, path, 0)
        return result

