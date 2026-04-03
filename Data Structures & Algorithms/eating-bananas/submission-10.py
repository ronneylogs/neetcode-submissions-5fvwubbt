class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l<=r:
            rate = (l+r) // 2
            time = 0

            for i in piles:
                time += math.ceil(i/rate)
            
            if time<=h:
                r = rate - 1
            else:
                l = rate + 1
        
            
        return l