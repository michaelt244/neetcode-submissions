class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1


        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]  # 1-indexed
            elif numbers[left] + numbers[right] < target:
                left += 1 # sum too small, move left up
            else: 
               right -= 1 # sum too big, move right up
        #no sum was found
        return []