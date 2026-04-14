class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []


        def backtracking(path,idx):
            res.append(path.copy())

            if idx>=len(nums):
                return
            
            for i in range(idx,len(nums)):
                path.append(nums[i])
                backtracking(path,i+1)
                path.pop()

            return
        

        backtracking([],0)
        
        return res