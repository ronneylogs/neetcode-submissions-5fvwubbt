class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # count how many times each task appears
        count = defaultdict(int)
        for i in tasks:
            count[i] += 1

        # build a max_heap
        max_heap = []
        
        for k,v in count.items():
            heapq.heappush(max_heap,-1*v)
        
        time = 0
        q = collections.deque() #stores pairs of [-cnt,idleTime]

        # if max_heap exists then that means thing could be in q
        # if q exists then that means
        while max_heap or q:
            time += 1

            # if heap isn't empty then we remove an item from the heap
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt,time+n])
            
            # if q exists and the first item is times up then we add the count to the q
            if q and q[0][1] == time:
                heapq.heappush(max_heap,q.popleft()[0])
        
        # return the total amount of time that it takes
        return time



        
