class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temps = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                temps[stackIndex] =  (i - stackIndex)
            stack.append([t, i])
        
        return temps
