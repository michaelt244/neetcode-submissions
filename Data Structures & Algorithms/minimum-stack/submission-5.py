class MinStack:

    def __init__(self):
        # Main stack to store all values
        self.stack = []
        # Parallel stack to track the current minimum at each prefix
        self.min_stack = []
        

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)
        
        # Update the min_stack with the new current minimum:
        # if min_stack is empty, current_min is val;
        # otherwise it's the min of val and the previous current minimum.
        current_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(current_min)
        

    def pop(self) -> None:
        # Pop from both stacks to keep them in sync
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Return the top value of the main stack
        return self.stack[-1]
        

    def getMin(self) -> int:
        # Return the top value of the min stack which is the smallest value by defult to get keep this O(1)
        return self.min_stack[-1]

        
