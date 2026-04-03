class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0] * len(temperatures)
        for i,x in enumerate(temperatures):
            
            if stack:
                while(stack and x > stack[-1][1]):
                    val = stack.pop()
                    res[val[0]] = i - val[0]
                stack.append((i,x))
            else:
                stack.append((i,x))
        
        return res
        


        # Input: an array of temperatures
        # Output: an array of the # of days before a warmer temperature appears

        # Idea is that:
        # Add item to stack
        # While stack is non empty, if top item is less than cur item, then pop up stack item, calculate the indices
        # and add to res array
        # Each item in the stack (temperature, indicies)
        