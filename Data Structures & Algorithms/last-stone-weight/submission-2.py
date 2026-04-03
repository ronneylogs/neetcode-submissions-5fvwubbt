class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while(len(heap)>1):
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            # Pop two and smash them, if there is remaining number then add it back
            print(first)
            if second > first:
                heapq.heappush(heap,first - second)

        heap.append(0)
        return abs(heap[0])
