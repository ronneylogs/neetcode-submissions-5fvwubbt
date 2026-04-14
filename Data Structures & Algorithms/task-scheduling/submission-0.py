class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = Counter(tasks)
        print(counter)
        max_heap = []

        for k,v in counter.items():
            heapq.heappush(max_heap,-1*v)

        q = collections.deque()

        time = 0
        while max_heap or q:
            time +=1

            if max_heap:
                c = 1+heapq.heappop(max_heap)
                if c:
                    q.append([c,time+n])
        
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap,q[0][0])
                q.popleft()

        return time   
            







        # Count the frequencies in a dictionary
        # Use a heap to store [Count of the item]
        

        # Use a queue for each item that needs to wait
        