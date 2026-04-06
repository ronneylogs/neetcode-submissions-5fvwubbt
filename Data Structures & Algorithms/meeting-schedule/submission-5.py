"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.start)
        if len(intervals) == 0:
            return True
        col = [intervals[0]]

        for i in intervals[1:]:
            if col[-1].end > i.start:
                return False
            col.append(Interval(i.start,i.end))
        
        return True




        # Idea is that a conflict is when end(first) > start(second)
        