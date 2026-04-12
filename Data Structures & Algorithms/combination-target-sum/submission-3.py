class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # nums.sort()

        def backtracking(path,total,idx):
            if total > target:
                return
            if total == target:
                res.append(path.copy())
                return

            for i in range(idx,len(nums)):
                path.append(nums[i])
                backtracking(path,total+nums[i],i)
                path.pop()


            return

    
        backtracking([],0,0)
        return res
        