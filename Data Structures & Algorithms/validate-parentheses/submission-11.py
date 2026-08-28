class Solution:
    def isValid(self, s: str) -> bool:

        bracket_dict = {"[":"]","{":"}","(":")"}
        stack = []
        for i in range(len(s)):
            if s[i] in bracket_dict:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if s[i] != bracket_dict[stack[-1]]:
                    return False
                
                
                stack.pop()
            
        
        if len(stack) == 0: return True

        return False

     



# Idea
# We travel from left to right of the string

# If opening bracket, we append to stack
# If closing bracket, we pop from stack and check if don't match
    # If yes then we return false

# At the end if the stack is not empty then we return false