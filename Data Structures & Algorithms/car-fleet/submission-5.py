class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Building a list of (position, speed) pairs for each car
        fleat = [[p, s] for p, s in zip(position, speed)]

        # Stack to hold the arrival time of each fleet's lead car
        stack = []

        # Sort cars by position in descending order (farthest to closest to target)
        # Then iterate through them
        for p, s in sorted(fleat)[::-1]: #revesre sorted order

            # Compute arrival time if this car never slows down
            stack.append((target - p)/s)

            # If current car's arrival time greater than or equal to previous car's arrival time,
            # it catches up and joins the fleet in front.
            # Remove the extra time entry so we keep only the lead time and pop the current one.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        # Return the number of fleets (each unique arrival time in stack)
        return len(stack)

        
                
            

            

        