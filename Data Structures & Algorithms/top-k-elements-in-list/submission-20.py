class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        tracker = {}


        for num in nums:
            
            if num not in tracker:
                tracker[num] = 1
            else:
                tracker[num] += 1

        
        sorted_hash = dict(sorted(tracker.items(), key=lambda x: x[1], reverse=True))

        return list(sorted_hash.keys())[:k]