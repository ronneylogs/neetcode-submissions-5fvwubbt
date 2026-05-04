class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(tot,path,idx):
            if tot == target:
                res.append(path.copy())
                return
            
            if tot > target:
                return

            for i in range(idx,len(nums)):
                path.append(nums[i])
                backtrack(tot+nums[i],path,i)
                path.pop()
            

        backtrack(0,[],0)
        return res

# choices at each step, could be itself or also anything latedr
# base is when our sum is equal or exceeds





        # idea: at each step my choice doesn't shrink, i can choose anything from 0 - n
        