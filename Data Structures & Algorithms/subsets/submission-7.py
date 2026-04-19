class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(i,path):
            res.append(path.copy())
            
            if i>=len(nums):
                return
            
            for j in range(i,len(nums)):
                path.append(nums[j])
                backtracking(j+1,path)
                path.pop()
            

        backtracking(0,[])
        return res




        # idea
        # options are the number of nums in the input
        # return at every possibility
        