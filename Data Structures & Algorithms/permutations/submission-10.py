class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        # keep track of elem used so far

        seen = [False] * len(nums)

        def dfs(path):

            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            if len(path) > len(nums):
                return

            
            for j in range(len(nums)):
                if not seen[j]:
                    path.append(nums[j])
                    seen[j] = True
                    dfs(path)
                    path.pop()
                    seen[j] = False



        
        dfs([])

        return res



        # can repeat in different ordering
        # choices: every number other than itself