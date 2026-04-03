class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r=0
        word_dict = defaultdict(int)
        res = 0
        while r<len(s):

            # Increment left
            while(word_dict[s[r]]==1):
                word_dict[s[l]] -= 1
                l += 1

            # Add to dictionary
            word_dict[s[r]] += 1

            # Record result
            res = max(res,r-l+1)
            r = r + 1
    
        return res





        # Idea
        # Dict to keep track of letters currently in string
        # If right pointer in already in string, 
        #   then increment left pointer until there is no repeating
        # Capture the result at the end of each loop
        