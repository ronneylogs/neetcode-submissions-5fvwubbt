class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        # Define our variables
        l = 0
        mySet = set()
        length = 0

        # For loop for going through array
        for r in range(len(s)):
            # while r_element is within set
            while s[r] in mySet:
                # remove l_element from set
                mySet.remove(s[l])
                # inc l
                l += 1
            
            # add r_element to set
            mySet.add(s[r])
            # update length
            length = max(length,r-l+1)
        

        return length
        # Sliding window
        # To keep track we will use a set

        # set={x,y,z}
        # length=3