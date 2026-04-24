"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key= lambda x: x.start)

        heap = []

        for i in intervals:

            if heap and heap[0] <= i.start:
                heapq.heappop(heap)
                heapq.heappush(heap,i.end)
            else:
                heapq.heappush(heap,i.end)
        
        return len(heap)




    # use a heap
    # if we can reuse the room then we remove a room and push, if not then we push to it
        
    # we only remove from the heap if there is no overlap
