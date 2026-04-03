class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])

        # first intput
        output = [intervals[0]]

        for start, end in intervals:
            # Grabs latest end time
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd,end)

            else:
                output.append([start,end])

        return output
        


        # Idea is that
        # sort list by their start times
        # iterate through sorted list

        # 