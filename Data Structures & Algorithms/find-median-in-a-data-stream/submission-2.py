class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []
        

    def addNum(self, num: int) -> None:
        
        #we alwasy push to the min heap first
        heapq.heappush(self.small, -1 * num)

        #check if the conditions are still valid after (the small_numbers[0] < big_numbers[0])

        if(self.small and self.large and (self.large[0] <  (-1 * self.small[0]))):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        #now we are handling uneven sizing so one is larger than the other


        #the large number heap is too big
        if (len(self.small) + 1 < len(self.large)):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val)
        
        #the samll number heap is too big
        if (len(self.large) + 1 < len(self.small)):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        

    def findMedian(self) -> float:

        #the first case is the odd case

        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return ((-1 * self.small[0]) + self.large[0]) / 2

        