class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mostFreq = 0
        l = 0
        count = {}
        res = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            mostFreq = max(mostFreq,count[s[r]])

            # Increment left
            while((r-l+1) - mostFreq > k):
                count[s[l]] -= 1
                l+=1
            # Update newest length
            res = max(res,r-l+1)
        
        return res


# Stale mostFreq may let an invalid window stay on screen, 
# but any length it allows is still a length that was possible 
# because mostFreq came from a real window earlier.





 