class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            item_1 = -1*heapq.heappop(max_heap)
            item_2 = -1*heapq.heappop(max_heap)
            diff = item_1 - item_2

            if diff == 0:
                continue
            else:
                heapq.heappush(max_heap,-1*diff)

        if len(max_heap) > 0:
            return -max_heap[0]

        return 0





        # at each step, take the two heaviest stones and smash them together
            # if equal weight then destroy
            # otherwise, the remaining weight of the survived is added back to the pile

        
