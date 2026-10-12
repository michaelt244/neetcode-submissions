class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i: [] for i in range(1,n + 1)}

        for src, dst, time in times:
            adj_list[src].append((time, dst))

        print(adj_list)

        shortest = {}
        minHeap = [(0, k)]

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            
            if node in shortest:
                continue
            shortest[node] = weight

            for neighbor_weight, neighbor_node in adj_list[node]:
                if neighbor_node not in shortest:
                    heapq.heappush(minHeap, (weight + neighbor_weight, neighbor_node))
        
        
        if len(shortest) != n:
            return -1

        return max(shortest.values())
        
        