"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        min_heap = []
        rooms = 0

        for interval in intervals:

            # we can remove an item
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,interval.end)
                

            # there is a conflict and we can't reuse a room for sure, increment the number of rooms that we need
            else:
                heapq.heappush(min_heap,interval.end)
                rooms = rooms+1

        
        return rooms

        