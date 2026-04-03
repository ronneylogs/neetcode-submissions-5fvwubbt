class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path):
            print(path)
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    dfs(path)
                    path.pop()
                
            
        dfs([])

        return res


        # Base case: 1. size of our path == nums

        # Choices: pick the number or don't pick the number
        