"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals):
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        rooms = 0
        max_rooms = 0
        end = 0

        for start in starts:
            if start >= ends[end]:
                end += 1
            else:
                rooms += 1

            max_rooms = max(max_rooms, rooms)

        return rooms

        