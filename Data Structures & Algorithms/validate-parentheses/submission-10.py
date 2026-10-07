class Solution:
    def isValid(self, s: str) -> bool:

        stacker = []
        # creating a map of closing brackets to their matching opening brackets
        close_to_open = {")": "(", "}": "{", "]": "["}


        for p in s:
            #if p is a our list check else skip
            #if p is a closer
            if p in close_to_open:
                #if the stack is 0 then that means we dont have a openinng return false
                #if the end of the stack doesnt match its opening return false
                if len(stacker) == 0 or stacker[-1] != close_to_open[p]:
                    return False
                #if it matches remove its opener
                stacker.pop()
            else:
                #if its a openining add it to the stack
                stacker.append(p)
        
        #if our stack is not 0 then we know it doesnt have enought pairs
        #so this is not a valid input
        return len(stacker) == 0
        


        
        