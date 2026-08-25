class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temps = []

        for i, temp in enumerate(temperatures):
            current_max = temp
            for j in range(i, len(temperatures)):
                if current_max < temperatures[j]:
                    temps.append(j + 1)
                    break
        return temps

            
