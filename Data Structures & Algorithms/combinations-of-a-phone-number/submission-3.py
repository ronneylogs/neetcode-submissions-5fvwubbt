class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        numChar = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"qprs","8":"tuv","9":"wxyz"}

        def backtracking(path,idx):
            if len(path) == len(digits):
                res.append(path)
                return
            
            for i in numChar[digits[idx]]:
                path = path+i
                backtracking(path,idx+1)
                path = path[:-1]

        
        if digits:
            backtracking("",0)

        return res
        