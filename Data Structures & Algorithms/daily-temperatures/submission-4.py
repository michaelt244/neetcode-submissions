class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temps = [0] * len(temperatures)
        stack = [] #(temp, index)

        for i, t in enumerate(temperatures):
            #while the stack has numbers and the current temperature
            # is greater than the last number
            while stack and t > stack[-1][0]:
                #if the current number is larger than the last 
                #number in the stack pop it
                stackTemp, stackIndex = stack.pop()

                #since the current temp is larger than the previous index
                #we found the day the next day with a warmer day

                #current index - stack index = the distance
                temps[stackIndex] =  (i - stackIndex)
            
            #add the number if its not larger
            stack.append([t, i])
        
        #return the temp it will default to 0 
        #for days that have no day after higher temperatures
        return temps
