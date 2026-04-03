class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1

        resArea = 0

        while l<r:
            curArea = min(heights[l],heights[r]) * (r-l)

            resArea = max(resArea,curArea)

            if heights[l] < heights[r]:
                l = l+1
            else:
                r = r-1
            
        return resArea

        

    

