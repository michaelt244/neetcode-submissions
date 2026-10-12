class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:


        adj_list = {i: [] for i in range(n)}

        for (src, dst), prob in zip(edges, succProb):
            adj_list[src].append((prob, dst))
            adj_list[dst].append((prob, src))
        

        #print(adj_list)
        shortest = {}
        print(adj_list[start_node])
        maxHeap = [(-1, start_node)]

        while maxHeap:
            prob, node = heapq.heappop(maxHeap)

            if node == end_node:
                return (-1 * prob)
            if node in shortest:
                continue
                
            shortest[node] = prob
            for neighbor_prob, neighbor_node in adj_list[node]:
                if neighbor_node not in shortest:
                    heapq.heappush(maxHeap, (neighbor_prob * prob, neighbor_node))
            
        
        print(shortest)
        if end_node not in shortest:
            return 0

        return (-1 * shortest[end_node])
        