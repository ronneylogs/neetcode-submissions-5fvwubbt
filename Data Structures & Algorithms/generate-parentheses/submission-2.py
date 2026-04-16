class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        options = ["(",")"]
        def backtrack(path,open,close):
            if close > open:
                return
            if n == open == close:
                print(path)
                res.append(path)
                return
            
            if len(path) > 2*n:
                return

            for i in range(len(options)):
                path = path + "".join(options[i])
                print(path)
                if options[i] == "(":
                    backtrack(path,open+1,close)
                else:
                    backtrack(path,open,close+1)
                path = path[:-1]
        

        backtrack("",0,0)
        return res

        

        # idea
        # what are my choices at each step? ( or ), but there only be maximum n of (
        #     use two variables open and close to keep track of brackets
        #         avoid exploring paths where close > open
        #     when string reaches 2n add to results

          
