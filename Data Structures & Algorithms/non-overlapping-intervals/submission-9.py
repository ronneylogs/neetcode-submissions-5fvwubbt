class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()


        res = 0


        for i in range(1,len(intervals)):
            if intervals[i][0] >= intervals[i-1][1]:
                intervals[i-1][1] = intervals[i][1]
            else:
                res +=1
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1])
            

        return res

        # 1,2 1,4 2,4


        # we want to maximize the amount of intervals, so sort by end
        # when items are sorted by the end, we are removing items based on the whichever one is freed up first
        
