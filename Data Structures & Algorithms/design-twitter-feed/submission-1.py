class Twitter:

    def __init__(self):
        self.count = 0

        # userId -> list of [count,tweetIds]
        self.tweetMap = defaultdict(list)

        # userId -> set of followeeId
        # Followee is something that i am following
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # User should always see their own tweets
        self.followMap[userId].add(userId)

        # Put each followee's most recent tweet into the heap
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # Repeatedly take the most recent tweet available
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            # Add the next older tweet from the same followee
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    # add followee to follower's follow-set
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)



    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
