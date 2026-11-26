class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()


        def dfs(curSum,path,i):
            if curSum == target:
                res.append(path.copy())
                return

            if curSum > target:
                return

            for j in range(i,len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                
                path.append(candidates[j])
                dfs(curSum+candidates[j],path,j+1)
                path.pop()
                



        dfs(0,[],0)
        
        return res

        # siblings can't be repeated
        # children yes