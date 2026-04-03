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

        s = 0
        e = 0
        neededRooms = 0
        res = 0

        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                neededRooms += 1
                s += 1
            else:
                neededRooms -= 1
                e += 1
            


            res = max(res,neededRooms)

        
        return res
            
        