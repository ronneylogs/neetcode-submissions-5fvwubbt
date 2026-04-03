"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])


        # captures final answer
        res = 0

        # captures intermediate answers
        count = 0

        s = e = 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            
            res = max(res,count)
        
        return res


        

        # separate into two timelines
            # start
            # end
        
        # rules
            # whenever a meeting starts before another one ends, we need a new room
            # whenever a meeting ends before at the same time another starts, a room becomes free
        # By moving two poitners over the sorted start and end times, we can track how many meetings are happening at the same time
        # max number of simultaneous meetinngs is the answer