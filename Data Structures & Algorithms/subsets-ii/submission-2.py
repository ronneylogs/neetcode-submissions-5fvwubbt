class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(path,i):
            res.append(path.copy())

            if i==len(nums):
                return
            

            for j in range(i,len(nums)):
                if j>i and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                dfs(path,j+1)
                path.pop()

            

        
        dfs([],0)

        return res



        # how can we avoid duplicates
        