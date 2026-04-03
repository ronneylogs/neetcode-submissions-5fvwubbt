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

        minHeap = []

        for i in intervals:
            if minHeap and minHeap[0] <= i.start:
                heapq.heappop(minHeap)
            
            # occupy a room
            heapq.heappush(minHeap,i.end)


        return len(minHeap)



        # Want to find the minimum # of meeting rooms required so that no meetings overlap

        # each meeting needs a room from its start time to its end time
        # if a meeting starts after or at the same time another meeting ends, they can share the same room
        # otherwise, we need a new room


        # use min heap to contain the endings
        # meetings that end later shall leave last
        # if the end time is less than the start time then we can remove the item from heap