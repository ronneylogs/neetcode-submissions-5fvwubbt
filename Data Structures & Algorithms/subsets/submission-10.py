class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path,i):
            

            res.append(path.copy())

            if i == len(nums):
                return
            
            for j in range(i,len(nums)):
                path.append(nums[j])
                dfs(path,j+1)
                path.pop()

    
            

        

        dfs([],0)

        return res
        


        # at each step what are my options
            # every succeeding other than myself

        # when are we done
            # we want to capture everything along the path