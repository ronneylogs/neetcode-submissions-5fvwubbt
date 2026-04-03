class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        curMax = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] += 1
            curMax = max(curMax,count[s[r]])

            while (r+1-l-curMax>k):
                count[s[l]] -= 1
                l += 1
                curMax = max(count.values()) if count else 0
            
            res = max(res,r-l+1)

        return res
                



        



 
#  Keep track of most frequent element
    # Would have to potentially update this each time we add an element
# Sliding window approach
    # Increment left whenever length of string - most frequent element > k
    # Increment right for each iteration