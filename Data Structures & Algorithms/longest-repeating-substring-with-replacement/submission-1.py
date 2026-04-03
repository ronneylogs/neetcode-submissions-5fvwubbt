class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myMap = {}

        res = 0 

        l = 0
        r = 0

        while(r<len(s)):
            myMap[s[r]] = 1 + myMap.get(s[r], 0)
            maxKey = max(myMap.values())
            
   
            if((r-l+1) - maxKey <= k):
                res = max(res, r-l+1)
            else:
                myMap[s[l]] -= 1
                l = l + 1
                
            r = r + 1
        return res