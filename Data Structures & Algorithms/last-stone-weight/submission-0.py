class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while(len(stones)>1):
            first = heapq.heappop(stones) * -1
            second = heapq.heappop(stones) * -1

            if first > second:
                heapq.heappush(stones,(first - second)*-1)

        stones.append(0)

        return abs(stones[0])