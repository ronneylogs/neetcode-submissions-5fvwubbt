class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(curSum,path,j):
            if curSum == target:
                res.append(path.copy())
                return

            if curSum > target:
                return
            
            for i in range(j,len(nums)):
                path.append(nums[i])
                dfs(curSum + nums[i],path,i)
                path.pop()



        dfs(0,[],0)

        return res

nums = [2,5,6,9]
target = 9

