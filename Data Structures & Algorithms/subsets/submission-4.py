class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [] # store subsets

        def backtrack(path, idx):
            res.append(path[:])
            # if at bottom of decision tree
            if idx == len(nums): 
                return
            # else explore other paths
            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()
            return
        
        backtrack([], 0)
        return res




        

        # Choices at each step:
            # choose the item or skip
        