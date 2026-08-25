class Solution:
    def findMin(self, nums: List[int]) -> int:


        left, right = 0, len(nums) - 1
        result = nums[left]



        while left <= right:
            #if its sorted left and right then the smallest value is the left most number since its sorted
            if nums[left] < nums[right]:
                result = min(result, nums[left])

                #break since you found the smallest value
                break
            

            middle = (left + right) // 2

            #check if the middle is the new smallest vlaue
            result = min(result, nums[middle])

            #if the left - middle is sorted then the right is unsorted (smallest value might be there)
            if nums[left] <= nums[middle]:
                left = middle + 1
            else:
                #if the left - middle is unsorted (smallest value will be in the left side)
                right = middle - 1
            
        return result

                
        