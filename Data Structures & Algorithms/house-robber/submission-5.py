class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1: return memo[i]
            
            memo[i] = max(dfs(i+1), dfs(i+2)+nums[i])

            return memo[i]
        
        return dfs(0)

        
        


        # What does dp(i) represents, it represents the total amount of houses 
            # you can rob at that point

        # Base case, we run out of houses

        # choices at each step
            # Rob the current house
            # Don't run current house