class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0] )
        res = [intervals[0]]

        i = 1

        while i<len(intervals):
            if res[-1][1] >= intervals[i][0]:
                minStart = min(res[-1][0],intervals[i][0])
                maxEnd = max(res[-1][1],intervals[i][1])
                res[-1][0] = minStart
                res[-1][1] = maxEnd
                i += 1
            else:
                res.append(intervals[i])
                i += 1
        
        return res
            




        # Idea is that
        # The first one is the default, and each time we move to the right
        # if first end time > second start time, we merge
        # each time we merge we want to add it to a final res

        # to deal with intervals that are not overlapping we can first add them to res, and at the end
            # merge them to res

        [1,3] [1,5]
        