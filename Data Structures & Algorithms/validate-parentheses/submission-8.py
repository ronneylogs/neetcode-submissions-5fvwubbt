class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {"(":")","[":"]","{":"}"}

        for i in s:
            if i == "[" or i=="{" or i=="(":
                stack.append(i)
            else:
                if len(stack)==0:
                    return False

                left = stack.pop()
                if match[left] != i:
                    return False
                # if left=="[" and i != "]":
                #     return False
                # if left=="{" and i != "}":
                #     return False
                # if left=="(" and i != ")":
                #     return False
        if len(stack) != 0: return False
        return True

        
        