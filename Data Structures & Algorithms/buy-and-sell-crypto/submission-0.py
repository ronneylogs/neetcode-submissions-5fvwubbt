class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        bestProfit = 0

        while(r<len(prices)):
            if prices[l] < prices[r]:
                bestProfit = max(bestProfit,prices[r] - prices[l])

            else:
                l = r

            r = r + 1
        
        return bestProfit



        # Steps -use l and r pointers
        # measure 
        # if l < r, measure profit and saved
        # else l = r
        # both: inc r

        