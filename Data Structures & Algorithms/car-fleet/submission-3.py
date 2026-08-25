class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleat = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(fleat)[::-1]: #revesre sorted order
            stack.append((target - p)/s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        
        return len(stack)

        
                
            

            

        