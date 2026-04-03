class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i =="{" or i=="[" :
                stack.append(i)
            else:
                try:
                    close = stack.pop()
                except:
                    return False
                if close == "(" and i!=")":
                    return False
                elif close == "{" and i!="}":
                    return False
                elif close == "[" and i!="]":
                    return False

        if stack:  
            return False
        return True

        # Input: a string of the parenthesis
        # Output: boolean of whether the parenthesis are valid or not

        # Condition of whether a parenthesis is valid is if:
            # it is the matching parenthesis
            # it is also the closing one


        # Idea of the algorithm
        # Read from left to right, if it is an opening parenthesis, add to the stack
            # else (it is a closing) we will be popping from the stack and checking if they are matching