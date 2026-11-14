class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count how many times each task appears
        count = defaultdict(int)
        for i in tasks:
            count[i] += 1
        
        # build max heap
        max_heap = []
        for k,v in count.items():
            heapq.heappush(max_heap, -v)

        # initiate time 
        time = 0

        # initiate deque
        q = collections.deque()

        # while both the heap and q exists
        # heap holds items that are ready to be processed
        # q holds items that are waiting to be processed
        while max_heap or q:
            
            # remove items from q
            if q and q[0][1] == time:
                heapq.heappush(max_heap,q.popleft()[0])


            # remove items from heap
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt,time+n+1])

            time += 1


    
        return time
        