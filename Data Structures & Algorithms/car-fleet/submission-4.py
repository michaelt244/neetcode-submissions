class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #getting a list [postion, speed]
        fleat = [[p, s] for p, s in zip(position, speed)]

        #our stack
        stack = []

        #going throught the sorted list in reverse order
        for p, s in sorted(fleat)[::-1]: #revesre sorted order

            #adding the postions speed
            stack.append((target - p)/s)

            #if the stack has more than two fleats and if the current speed is less
            #than the top of the stack pop it off since it will create a fleat
            #with a fleat already in the stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        #return the lenght of the stack which is the number of fleats we have
        return len(stack)

        
                
            

            

        