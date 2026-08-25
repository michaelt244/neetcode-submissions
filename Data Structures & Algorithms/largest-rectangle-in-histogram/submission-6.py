class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #pair(index, heigh)
        maxarea = 0

        for i, h in enumerate(heights):
            #starting value
            start = i
            #while the stack is not empty and the next height is smaller()
            #we will be popping from the stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop() #saving the values

                #calculating the maxarea (heigth * currnetindex - index in the stack)
                maxarea = max(maxarea, height * (i - index))

                #the new start is the index in the previous index
                start = index
            #appending to the stacK
            stack.append((start, h))
        
        #this is for the left over values in the histagram
        for i, h in stack:
            #caluclating the area using the height and then the width calulcated by len(height) - i(index)
            maxarea = max(maxarea, h * (len(heights) - i ))
        
        return maxarea

                
            