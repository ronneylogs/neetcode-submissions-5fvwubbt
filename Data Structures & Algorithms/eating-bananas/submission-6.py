class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ret = float('inf')

        while l<=r:
            m = (l+r) // 2
            x = 0

            for i in piles:
                x += math.ceil(i/m)
                
            print('x',x)
            print('m',m)
            if x<=h:
                ret = min(ret,m)

            if x<=h:
                r = m - 1
            else:
                l = m + 1
        
            
        return ret