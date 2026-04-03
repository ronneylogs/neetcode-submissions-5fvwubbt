class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(path,i,total):
            if total==target:
                res.append(path.copy())
                return
            
            if total > target or i>=len(nums):
                return
            
            path.append(nums[i])
            dfs(path,i,total+nums[i])
            path.pop()
            dfs(path,i+1,total)

        dfs([],0,0)

        return res


            
        


        # choices are
            # picking the number or not picking it

        # base case is if the total adds up to target