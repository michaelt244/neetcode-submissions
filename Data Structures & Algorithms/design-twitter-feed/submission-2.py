class Twitter:

    def __init__(self):
        self.count = 0 #how many tweets they have seen
        self.tweetMap = defaultdict(list) #going to be a minheap based on the lastest tweet they seen (time, tweet_id)
        self.followMap = defaultdict(set) #set of people they follow {michael:his followers}

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Use negative count so min-heap acts like a max-heap (latest first)
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1


        

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        recent_heap = []

        #ensure user is in their own feed
        self.followMap[userId].add(userId)

        for followeID in self.followMap[userId]:
            if followeID in self.tweetMap:
                index = len(self.tweetMap[followeID]) - 1
                
                count, tweetID = self.tweetMap[followeID][index]
                heapq.heappush(recent_heap, [count, tweetID, followeID, index - 1])
                
        while recent_heap and len(result) < 10:
            #need to get the user_id to save it 
            count, tweetID, followeID, index = heapq.heappop(recent_heap)
            result.append(tweetID)

            if index >= 0:
                next_count, next_tweetID = self.tweetMap[followeID][index]
                heapq.heappush(recent_heap, [next_count, next_tweetID, followeID, index - 1])

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # You cannot unfollow yourself in most test cases
        if followeeId in self.followMap[followerId] and followerId != followeeId:
            self.followMap[followerId].remove(followeeId)
        
