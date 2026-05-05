class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        res = []

        def backtrack(path,i):
            if i == len(digits):
                res.append(path)
                return

            for d in letterMap[digits[i]]:
                path += d
                backtrack(path,i+1)
                path = path[:-1]


        if digits:
            backtrack("",0)

        return res


        # choices at each step: All the choices for the number that we are at
        # base case: if path size is equal to number of digits
        