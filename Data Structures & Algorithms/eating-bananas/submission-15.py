class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = max(piles)

        while l <= r:
            rate = (l + r) // 2
            time = sum((p + rate - 1) // rate for p in piles)

            if time <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1

        return res
        