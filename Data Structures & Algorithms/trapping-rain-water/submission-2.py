class Solution:
    def trap(self, height: List[int]) -> int:

        prefix = [0] * len(height)
        suffix = [0] * len(height)

        # maxL = 0
        # maxR = 0

        prefix[0] = height[0]
        for i in range(1,len(height),1):
            prefix[i] = max(prefix[i-1],height[i])

        suffix[-1] = height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            suffix[i] = max(suffix[i+1],height[i])
        
        total = 0
        # Iterate over prefix and suffix to grab the min and minus height
        for i in range(len(height)):
            total += min(prefix[i],suffix[i]) - height[i]

        
        return total




# Idea is that:
# Build a prefix and suffix list
#   Each item in the list should be the max of everything including itself
        