class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        count = 0
        fleat = list(zip(position, speed))

        fleat = sorted(fleat, key=lambda x: x[0], reverse=True)

        for i in range(len(position), 0):
            time = (target - position[i]) / speed[i]
            fleat.append

        
                
            

            

        