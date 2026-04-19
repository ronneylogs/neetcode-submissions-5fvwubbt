class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitToChar = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"prqs","8":"tuv","9":"wxyz"}

        def backtrack(i,path):
            if i==len(digits):
                res.append(path)
                return

            for c in digitToChar[digits[i]]:
                path += c
                backtrack(i+1,path)
                path = path[:-1]
                
        if digits:
            backtrack(0,"")

        return res

# "34"
# 0 "", for c in d,e,f
#     1, "d", for c in g,h,i
#         2, "dg", add path
#         2, "dh", add path
#         2, "di", add path
#     1, "e"
#     1, "f"


        
        
        