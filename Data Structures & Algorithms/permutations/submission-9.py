class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(i,path):

            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            if len(path) > len(nums):
                return

            
            for j in range(len(nums)):
                if nums[j] in path:
                    continue
                path.append(nums[j])
                dfs(i,path)
                path.pop()



        
        dfs(0,[])

        return res



        # can repeat in different ordering
        # choices: every number other than itself