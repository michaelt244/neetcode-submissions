class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distance = []
        heapq.heapify(distance)
        for x, y in points:
            heapq.heappush(distance,(- 1 * math.sqrt((x ** 2) + (y ** 2)), (x, y)))

            if len(distance) > k:
                heapq.heappop(distance)

        result = []
        while distance:
            dist, (x, y) = heapq.heappop(distance)
            result.append([x,y])
        
        return result