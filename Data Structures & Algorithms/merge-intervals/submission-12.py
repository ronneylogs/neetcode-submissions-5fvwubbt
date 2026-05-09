class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])

        res = [intervals[0]]

        for i in range(1,len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                print(res)
                max_end = max(res[-1][1],intervals[i][1])
                res[-1][1] = max_end
                print(res)
            else:
                
                res.append(intervals[i])
            
        
        return res

        # idea: Sort all interval by it's starting position
            # walk through each interval, if they overlap then merge