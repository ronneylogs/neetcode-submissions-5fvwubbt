class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 1

        res = 0
        count = defaultdict(int)
        count[s[l]] += 1


        while(r<len(s)):
            count[s[r]] += 1
            maxF = max(count.values())

            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res,r-l+1)

            r = r+1
            

        return res


 