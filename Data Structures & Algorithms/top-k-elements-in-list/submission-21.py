class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        tracker = {}
        for num in nums:
            if num not in tracker:
               tracker[num] = 1
            else:
                tracker[num] += 1
        #sorted_hash = dict(sorted(tracker.items(), key=lambda x: x[1], reverse=True))
        #return list(sorted_hash.keys())[:k]


        #most optimal appreach using bucket sort(hint given the)
        
        bucket = [[] for i in range(len(nums) + 1)]

        for num, freq in tracker.items():
            bucket[freq].append(num)
        
        ans = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

