class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftPos= [-1] * len(heights)
        rightPos = [len(heights)] * len(heights)
        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftPos[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightPos[i] = stack[-1]
            stack.append(i)
        
        maxArea = 0
        for i in range(len(heights)):
            leftPos[i] += 1
            rightPos[i] -= 1

            area = heights[i] * (rightPos[i] - leftPos[i] + 1)
            maxArea = max(maxArea,area)
        
        return maxArea




        # Idea is that
            # build a left and right array
            # Each array gives the farthest index that satisfies the rectangle

        # Use a increasing stack
        # At the end calculate the area