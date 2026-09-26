class TimeMap:

    def __init__(self):
        self.map = {} #vlaue list, timestamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.map:
            return ""
        
        values = self.map.get(key)
        left, right = 0, len(values) - 1

        previous_timestamp = ""

        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] == timestamp:
                return values[middle][0]

            elif values[middle][1] > timestamp:
                right = middle - 1
            else:
                previous_timestamp = values[middle][0]
                left = middle + 1
        #should return the second lowest if its not found
        return previous_timestamp
