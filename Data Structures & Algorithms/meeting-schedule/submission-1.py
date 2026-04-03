"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda i: i.start)


        print(intervals)

        for i in range(1,len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]

            if i2.start < i1.end:
                return False
        
        return True





        # Idea is that
        # there is a conflict if start of second interval is less than the end value of the first interval
