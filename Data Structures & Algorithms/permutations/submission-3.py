class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path,i):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for z in nums:
                if z not in path:
                    path.append(z)
                    dfs(path,i)
                    path.pop()
            
        

        dfs([],0)
        return res
        





        # Base case: the length is equal to nums
        # Choices at each step
            # choose another number other than itself
