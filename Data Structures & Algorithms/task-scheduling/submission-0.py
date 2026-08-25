class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency_table = {}
        for task in tasks:
            if task not in frequency_table:
                frequency_table[task] = 1
            else:
                frequency_table[task] += 1
        

        maxHeap = [[-cnt, task] for task, cnt in frequency_table.items()]
        heapq.heapify(maxHeap)

        waiting_period = deque()
        current_time = 0 
        

        while maxHeap or waiting_period:
            
            #increaseing the total time
            current_time += 1

            #popping the highest frequency letter from the heap
            if maxHeap:
                count, letter = heapq.heappop(maxHeap)
                #decrease current count(negative so increase it to account for the fact we removed it once)
                count += 1

                if count < 0:
                    waiting_period.append((count, letter, current_time + n)) #current_time + n is when it will be ready to use again

            if waiting_period and waiting_period[0][2] == current_time: 
                count, letter, ready_time = waiting_period.popleft()
                heapq.heappush(maxHeap, [count, letter])
    
        return current_time



        