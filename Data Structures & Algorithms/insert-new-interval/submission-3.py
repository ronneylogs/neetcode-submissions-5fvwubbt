class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, (start, end) in enumerate(intervals):
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
        
            
            elif newInterval[0] > end:
                res.append([start,end])

            else:
                newInterval = [
                    min(newInterval[0],start),
                    max(newInterval[1],end)
                ]

        res.append(newInterval)
                

        return res





        # Go through the intervals, and always compare the end of curInterval with start of newInterval

        # Three possible scenarios:
        # 1. newInterval is behind the curInterval
        #     we can insert easily

        # 2. newInterval is after the curInterval
        #     we can insert easily

        # 3. newInterval is overlapping
        #     take the smallest start and largest end


        # We would need to initalize a new array to keep track of the new list
        