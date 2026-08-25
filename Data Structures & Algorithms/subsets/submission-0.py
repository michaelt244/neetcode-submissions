class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []



        path = []
        def dfs(i):
            if i >= len(nums):
                result.append(path.copy())
                return #out of bouds

            # including nums[i]
            path.append(nums[i])
            dfs(i + 1)

            # decesion not to include nums
            path.pop()
            dfs(i + 1)
        

        dfs(0)
        return result
            



        