class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        word_set = set()
        res = 0
        while r<len(s):

            # Increment left
            while s[r] in word_set:
                word_set.remove(s[l]) 
                l = l + 1
            
            # Add to dictionary
            word_set.add(s[r])


            # Record 
            res = max(res,r-l+1)
            r = r + 1
        
        return res




  




        # Idea
        # Set to keep track of character that's already shown up
