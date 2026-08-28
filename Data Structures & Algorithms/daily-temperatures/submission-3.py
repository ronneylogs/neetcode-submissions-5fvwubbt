class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = len(temperatures) * [0]

        for x in range(len(temperatures)):
            t = temperatures[x]
            if len(stack) == 0:
                stack.append((t,x))
                continue

            while len(stack)>0 and t > stack[-1][0]:
                n = stack.pop()
                res[n[1]] = x - n[1]


            stack.append((t,x))


        return res

# idea
# use a stack to keep track days that are still waiting for a warmer temperature
# go through temperatures
    # while cur temperature > top of stack:
        # pop top of stack and record the value (number of pops needed to reach that day)



# Input: temperatures = [30,38,30,36,35,40,28]

# [38]40
# [1,,1,2,1,,]

