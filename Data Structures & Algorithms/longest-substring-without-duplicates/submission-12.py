class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1

            seen.add(s[r])
            res = max(res,r-l+1)
        
        return res
            

        
  



    # Have a set to keep track of chars that are already seen
    # Each time we encounter a char that is seen, inc left pointer and remove 
        # from set until right pointer char can be inserted into set
    # Have a max value to keep track of longest substring