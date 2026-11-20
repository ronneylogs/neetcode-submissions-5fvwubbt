class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i,(start,end) in enumerate(intervals):
            # new is before
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]

            # new is after
            elif newInterval[0] > end:
                res.append([start,end])

            # overlaping
            else:
                newInterval = [
                    min(newInterval[0],start),
                    max(newInterval[1],end)
                ]
                
        res.append(newInterval)
        return res




        