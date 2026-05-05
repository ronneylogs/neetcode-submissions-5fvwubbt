class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = [-s for s in stones]
        heapq.heapify(stone)

        print(stone)

        while len(stone)>=2:
            s1 = -1*heapq.heappop(stone)
            s2 = -1*heapq.heappop(stone)

            if s2:
                n = s1-s2
                if n==0:
                    continue
                heapq.heappush(stone,-1*n)
        
        if stone:
            return -1*stone[0]
        else:
            return 0
        