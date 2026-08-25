class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temps = []

        for i, temp in enumerate(temperatures):
            current_max = temp
            z = 0
            for j in range(i, len(temperatures)):
                if current_max < temperatures[j]:
                    z = j
                    current_max = temperatures[j]
                    break
            if current_max == temp:
                temps.append(0)
            else:
                temps.append(z - i)
        return temps

            
