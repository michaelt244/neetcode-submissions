class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return None
        

        right  = len(nums1)
        temp = 0
        idx = 0 

        while(idx < n + m):
            if nums1[idx] > nums2[idx]:
                temp = nums1[idx]
                nums1[idx] = nums2[idx]
                idx += 1
                nums1[idx] = temp
            else:
                temp = nums2[idx]
                nums1[idx] = nums1[idx]
                idx += 1
                nums1[idx] = temp


        