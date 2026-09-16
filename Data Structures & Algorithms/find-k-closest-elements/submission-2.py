class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        left, right = 0, len(arr) - 1

        result = []
        
        #using binary search find the postion where the target would be 
        #this puts in cloest postion to the targer
        while left <= right:
            middle = (left + right) // 2

            if arr[middle] == x:
                left = middle
            elif arr[middle] < x:
                left = middle + 1 
            else:
                right = middle - 1

        l, r = left - 1, left

        while len(result) < k:
            if l < 0:
                result.append(arr[r])
                r += 1
            elif r >= len(arr):
                result.append(arr[l])
                l -=1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                result.append(arr[l])
                l -= 1
            else:
                result.append(arr[r])
                r +=1

        return sorted(result)


        

        