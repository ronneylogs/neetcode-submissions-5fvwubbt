class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dfs(i):
            if i>=len(nums):
                return 0

            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(dfs(i+1),nums[i]+dfs(i+2))
            return memo[i]
        
        return dfs(0)
        




# array nums, represents the amount of money the ith house has
# the ith house is the neighbour of the i-1th and i+1th house
# cannot rob two adjacent houses

# choices: can either rob the current one or rob the next one
# dp(i) represents the maximum amount of money that can be robbed at the ith index