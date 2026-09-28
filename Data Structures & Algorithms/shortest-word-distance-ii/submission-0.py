class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.index_map = {} #word: list of indices

        for index, word in enumerate(wordsDict):
            if word not in self.index_map:
                self.index_map[word] = []
            self.index_map[word].append(index)
        

    def shortest(self, word1: str, word2: str) -> int:
        #checking for constraints
        if word1 == word2:
            return

        if word1 not in self.index_map or word2 not in self.index_map:
            return 

        word1_indices = self.index_map[word1]
        word2_indices = self.index_map[word2]

        p1, p2 = 0, 0
        min_dist = float('inf')

        while p1 < len(word1_indices) and p2 < len(word2_indices):
            min_dist = min(min_dist, abs(word1_indices[p1] - word2_indices[p2]))

            if word1_indices[p1] > word1_indices[p2]:
                p2 += 1
            else:
                p1 += 1
        
        return min_dist



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
