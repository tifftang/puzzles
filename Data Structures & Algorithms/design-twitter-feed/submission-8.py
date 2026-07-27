class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followers[userId].add(userId)
        results = []
        heap = []
        for user in self.followers[userId]:
            if len(self.posts[user]) > 0:
                heapq.heappush(heap, (-self.posts[user][-1][0], len(self.posts[user]) - 1, user))
        
        while len(results) < 10 and heap:
            _, idx, user = heapq.heappop(heap)
            results.append(self.posts[user][idx][1])
            if idx > 0:
                heapq.heappush(heap, (-self.posts[user][idx - 1][0], idx - 1, user))
        return results

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
