class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i,path):
            if i >= len(s):
                res.append(path.copy())
                return
            
            
            for j in range(i,len(s)):
                if self.isPali(i,j,s):
                    path.append(s[i:j+1])
                    backtrack(j+1,path)
                    path.pop()
        
        backtrack(0,[])
        return res


    def isPali(self, l, r,s):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        

        # idea
        # the number of remaining options


    # def backtrack(start):
    #     if done:
    #         save answer
    #         return

    #     for each choice:
    #         if choice is valid:
    #             choose
    #             backtrack(next state)
    #             unchoose