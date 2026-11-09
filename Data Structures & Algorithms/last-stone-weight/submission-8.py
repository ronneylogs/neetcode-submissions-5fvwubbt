class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        arr = []
        for i in range(len(stones)):
            arr.append(-stones[i])
        heapq.heapify(arr)

        while len(arr) >= 2:
            item1 = -heapq.heappop(arr)
            item2 = -heapq.heappop(arr)

            if item1 > item2:
                res = item1 - item2
                if res != 0: heapq.heappush(arr,-res)
            else:
                res = item2 - item1
                if res != 0: heapq.heappush(arr,-res)
            
        if len(arr) > 0:
            return -arr[0]
        else:
            return 0

        

        # heapq.heappush(heap,item)
        # heapq.heappop(heap)
        # heapq.heapify(heap)


        # Idea, at each step we want the heaviest stone, we can use a heap to track of the heaviest stones at all times
            # keep smashing the two heaviest stones until only <2 remain


        # 1. Initiate an array to use as the heap
        # 2. Add items to the array, then run heapify on it
        # 3. While the heap size is greater >= 2
        #     - take two largest and smash them, if not 0 then add it back to the heap
        # 4. Return weight of last remaining stone or return 0 if none remain