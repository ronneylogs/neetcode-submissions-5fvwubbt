class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        res = [intervals[0]]

        for i in range(1,len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                lowest = min(intervals[i][0],res[-1][0])
                highest = max(intervals[i][1],res[-1][1])
                res[-1] = [lowest,highest]
            else:
                res.append(intervals[i])
    
        return res
        