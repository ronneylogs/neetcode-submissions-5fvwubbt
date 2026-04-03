class Solution:
   def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(added,path,i):
            if added == target:
                res.append(path.copy())
                return
            if added > target or i>=len(nums):
                return
            
            path.append(nums[i])
            dfs(added+nums[i],path,i)
            path.pop()
            dfs(added,path,i+1)


        dfs(0,[],0)
        
        return res


    # Base case: if target == sum, add to path
                # or if sum > target, return
            




        
        