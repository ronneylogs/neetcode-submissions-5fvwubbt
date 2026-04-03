class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for i in s:
            if i in closeToOpen:
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False

        # Input: a string of the parenthesis
        # Output: boolean of whether the parenthesis are valid or not

        # Condition of whether a parenthesis is valid is if:
            # it is the matching parenthesis
            # it is also the closing one


        # Idea of the algorithm
        # Read from left to right, if it is an opening parenthesis, add to the stack
            # else (it is a closing) we will be popping from the stack and checking if they are matching