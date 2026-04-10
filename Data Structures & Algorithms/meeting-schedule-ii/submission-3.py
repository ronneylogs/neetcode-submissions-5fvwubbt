"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        # imagine that heap as the rooms that need freeing, the number of unfreed rooms is the number of rooms we need
        min_heap = []
        max_rooms = 0

        for interval in intervals:
            
            if min_heap and min_heap[0] <= interval.start:
                # free a room
                # a meeting ends before new one starts
                heapq.heappop(min_heap)

            # add current room
            # Idea: A new meeting starts before any current meeting has ended.
            heapq.heappush(min_heap, interval.end)

            max_rooms = max(max_rooms, len(min_heap))

        return max_rooms