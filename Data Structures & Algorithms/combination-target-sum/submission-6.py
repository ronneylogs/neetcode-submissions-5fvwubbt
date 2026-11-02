class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(path,pSum,j):
            if pSum == target:
                res.append(path.copy())

            if pSum > target:
                return

            for i in range(j,len(nums)):
                path.append(nums[i])
                dfs(path,pSum + nums[i],i)
                path.pop()
                



        dfs([],0,0)

        return res






        # base case: when sum == target: add that to our res

        # choices: for loop over all choices