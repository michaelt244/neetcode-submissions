class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        path = []
        used = set()
        
        
        def backtracking():

            #base case if the path is ready to append
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for num in nums:
                if num in used:
                    continue
                
                path.append(num)
                used.add(num)

                backtracking()

                path.pop()
                used.remove(num)
        

        backtracking()
        return result