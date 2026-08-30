class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []


        ret = [0] * len(temperatures)

        for i,v in enumerate(temperatures):
            

            while stack and stack[-1][1] < v:
                item = stack.pop()
                ret[item[0]] = i - item[0]

            stack.append((i,v))
        
        return ret



    # [,]

    # [1]



        # Idea: use a stack
            #  think of the stack as a waiting room of days where there has not been a warmer temperature
            # monotonic stack


            # Go through each temperature
                # While it's greater than top of stack
                    # pop
                    # and fill out ret
                
                # append stack
            
            # return ret

        
        # For each day we want to know, when is the next day that is warmer than today

        # Brute force is to scan forward from every single day