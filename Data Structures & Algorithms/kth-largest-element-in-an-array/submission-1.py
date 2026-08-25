class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        #using max heap 
        #nums = [-n for n in nums]
        #heapq.heapify(nums)

        #for i in range(k - 1):
            #heapq.heappop(nums)
        
        #return -1 * heapq.heappop(nums)


        #uisng min heap
        minheap = []
        heapq.heapify(minheap)

        for num in nums:
            heapq.heappush(minheap, num)

            if len(minheap) > k:
                heapq.heappop(minheap)
        
        #return minheap[0] 
        return heapq.heappop(minheap)