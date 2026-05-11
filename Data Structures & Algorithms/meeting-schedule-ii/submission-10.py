"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        heap = []
        intervals.sort(key=lambda x: x.start)
        heap.append(intervals[0].end)
        for i in range(1,len(intervals)):

            if intervals[i].start < heap[0]:
                heapq.heappush(heap,intervals[i].end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap,intervals[i].end)
        
        return len(heap)



        # idea: sort everything interval by it's start time

        # Walk through each item
        # if overlapping, increase meeting rooms by one
            # otherwise, subtract a meeting room 
        

        # use a heap to track this kind of behaviour
            # pop interval from heap if can reuse the room