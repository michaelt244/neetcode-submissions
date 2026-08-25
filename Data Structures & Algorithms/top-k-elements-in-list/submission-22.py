class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        tracker = {}
        #mapping the number to its freq count
        for num in nums:
            if num not in tracker:
               tracker[num] = 1
            else:
                tracker[num] += 1
        #sorted_hash = dict(sorted(tracker.items(), key=lambda x: x[1], reverse=True))
        #return list(sorted_hash.keys())[:k]


        #most optimal appreach using bucket sort(hint given the)
        
        bucket = [[] for i in range(len(nums) + 1)]

        #item gives us the key-value pairs (1,3), (2, 2), (3,1)...
        for num, freq in tracker.items():
            bucket[freq].append(num) #adding the number to the freq list (a list since more than one number can have teh same freq)
        
        #final list
        ans = []

        #reverse from the back (back is highest freqy, front is the lowest freq)
        for i in range(len(bucket) - 1, 0, -1):
            #getting only valid items
            for num in bucket[i]:
                ans.append(num)
                #if we reacht the desered amount returm it
                if len(ans) == k:
                    return ans

