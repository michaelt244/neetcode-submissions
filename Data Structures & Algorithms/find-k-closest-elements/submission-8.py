class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        left, right = 0, len(arr) - 1

        result = []
        
        #using binary search find the postion where the target would be 
        #this puts in cloest postion to the targert so after the loop left is the first index where arr[left] >= x and right would be the last index where arr[right] < x
        while left <= right:
            middle = (left + right) // 2

            # If arr[middle] is less than x, x must be to the right.
            if arr[middle] < x:
                left = middle + 1 
            else:
                # arr[middle] >= x, so x could be at middle
                # or somewhere to its left.
                right = middle - 1

        l, r = left - 1, left
        
        # Choose exactly k elements.
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

        # Elements may have been selected from both directions,
        # so sort them before returning.
        return sorted(result)


        

        