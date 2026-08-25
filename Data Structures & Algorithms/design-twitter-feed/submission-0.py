class Twitter:

    def __init__(self):
        self.count = 0 #how many tweets they have seen
        self.tweetMap = defaultdict(list) #going to be a minheap based on the lastest tweet they seen (time, tweet_id)
        self.followMap = defaultdict(list) #set of people they follow {michael:his followers}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweetMap[userId].append([1 * self.count, tweetId])

        

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        recent_heap = []

        for person in self.followMap.values():
            #get the last tweet in each persons tweetMap
            start = len(self.tweetMap[person] - 1)
            tweet = self.tweetMap[person][index]

            recent_heap.append(tweet)

        recent_heap.append(self.tweetMap[userId][len(self.tweetMap[userId]- 1)])

        heapq.heapify(recent_heap)
        
        while len(result) < 10:
            #need to get the user_id to save it 
            person, index = heapq.heapop(recent_heap)

            if self.tweetMap[person]:
                index -= 1 
                tweet = self.tweetMap[person][index]
                heapq.heappush(recent_heap, tweet)
        

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if follwer_id and followeeId not in self.followMap:
            self.followMap[followerId] = [followeeId]
        else:
            self.followMap[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if follwer_id and followeeId not in self.followMap:
            return #not in the map
        self.followMap[followerId].remove(followeeId)
        
