class Solution:
    def isValid(self, s: str) -> bool:

        stacker = []
        close_to_open = {")": "(", "}": "{", "]": "["}


        for p in s:
            if p in close_to_open:
                if len(stacker) == 0 or stacker[-1] != close_to_open[p]:
                    return False
                stacker.pop()
            else:
                stacker.append(p)
        
        return len(stacker) == 0
        


        
        