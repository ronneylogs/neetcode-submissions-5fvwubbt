class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        collect = [intervals[0]]

        res = 0

        for start,end in intervals[1:]:
            # non overlapping
            if collect and collect[-1][1] <= start:
                collect.append([start,end])

            # overlapping
            else:
                collect.append([start,min(end,collect[-1][1])])
                res += 1

        
        return res
    