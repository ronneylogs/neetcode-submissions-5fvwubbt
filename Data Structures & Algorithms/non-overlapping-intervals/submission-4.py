class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])

        print(intervals)

        collect = [intervals[0]]
        res = 0
        for start,end in intervals[1:]:
            if collect and collect[-1][1] <= start:
                collect.append([start,end])
            else:
                collect.append([start,min(end,collect[-1][1])])
                res += 1


        return res
        # sort everything
        # add first item to collect
        # go through each item in the interval if it violates overlapping condition then lets remove it
        # everytime we are checking with the latest item from collectt
        