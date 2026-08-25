class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        nums.sort()
        result = []
        path = []
        

        def backtracking(i):
            if i >= len(nums):
                result.append(path.copy())
                return #index out of range
            

            #two branch strucutre 1 - inlcude number, 2 - skip duplicates

            
            path.append(nums[i])
            backtracking(i + 1)
            path.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtracking(i + 1) 
        
        backtracking(0)
        return result