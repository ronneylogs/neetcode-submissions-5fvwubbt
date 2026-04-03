class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        l = 0
        mySet = set()

        for r in range(len(s)):
            while s[r] in mySet:
                mySet.remove(s[l])
                l +=1
            mySet.add(s[r])
            res = max(res,r-l+1)
        
        return res


    



    # Input is a string, output is a number which is 
        # the longest substring where there are no repeats

    # Brute force method is to start at every index and 
        # keep extending until we see a repeated character

        # But this would be highly inefficient and result in a time of O(n^2)

    # Efficient method is to go with a sliding approach
        # Keep a sliding window that can grow and shrink
            # if valid then keep growing
            # if non valid then shrink
    
    # Time complexity would be O(n) as the window only goes through the string once

    
