class Solution:
    def search(self, nums: List[int], target: int) -> int:

      low, high = 0, len(nums) - 1
      
      while low <= high:

        middle = (low + high) // 2
        if nums[middle] == target:
          return middle
        #middle is to big so move it down
        elif nums[middle] > target:
          high = middle - 1
        #middle is to low so move it up
        else:
          low = middle + 1
        
      return -1