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
        
        left, right = 0, len(self.map[key]) - 1
        previous_timestamp = ""

        while left <= right:
            middle = (left + right) // 2
            if self.map[key][middle][1] == timestamp:
                return self.map[key][middle][0]
            elif self.map[key][middle][1] > timestamp:
                right = middle - 1
            else:
                left = middle + 1
                previous_timestamp = self.map[key][middle][0]
        #should return the second lowest if its not found
        return previous_timestamp
