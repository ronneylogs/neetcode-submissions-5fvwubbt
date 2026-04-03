class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Define variables
        l = 0
        myDict = defaultdict(int)
        length = 0
        maxChar=""

        # For loop
        for r in range(len(s)):
            myDict[s[r]] += 1
            maxChar = max(myDict, key=myDict.get)
            while(r-l+1-myDict[maxChar] > k):
                myDict[s[l]] -= 1
                l += 1
                maxChar = max(myDict, key=myDict.get)
            
            length = max(length,r-l+1)

        return length




# Sliding Window Approach
# Length: 4
# Dictionary to keep track of how many times each character in our window
#   is repeated {X:1,Y:2}
# maxChar:Y
# Conditions
    # inc l: length - maxChar# > k
    # inc r: after every iteration

# Time complexity: O(N)
# Space complexity: O(26)