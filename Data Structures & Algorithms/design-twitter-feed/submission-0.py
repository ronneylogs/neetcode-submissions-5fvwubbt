class Twitter:

    def __init__(self):
        self.count = 0

        # each person should have a list of people that they follow
        # userId -> set of followeeId
        self.followMap = defaultdict(set)

        # each person should have a list of posts that they made
        # userId -> list of [count,tweetIds]
        self.tweetMap = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        # user should always see their own tweets
        self.followMap[userId].add(userId)
        # populate heap first
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) -1
                count, tweetId = self.tweetMap[followee][index]
                heapq.heappush(heap,[count,tweetId,followee,index-1])

        while heap and len(res) < 10:
            count, tweetId,followee,index = heapq.heappop(heap)

            res.append(tweetId)

            if index>=0:
                count , tweetId = self.tweetMap[followee][index]
                heapq.heappush(heap,[count,tweetId,followee,index-1])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        

# idea is that
    # each followee is it's own list
        # each list has it's own list as well