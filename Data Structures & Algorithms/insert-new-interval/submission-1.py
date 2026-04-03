class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []



        # add all intervals that end before new interval starts to res
        while i<n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1


        # For all intervals that overlap with new interval
        # condition is if the end time of new interval is greater than the start time of interval
        while i<n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i += 1

        res.append(newInterval)
        print(res)


        # all intervals that start after new interval ends
        while i<n:
            res.append(intervals[i])
            i +=1 


        return res