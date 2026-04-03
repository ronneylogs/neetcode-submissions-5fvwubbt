class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        if len(nums) == 1:
            return nums[0]
        def dfs(i,c):
            if i >= len(nums) or (c==1 and i==len(nums)-1):
                return 0
            if (i,c) in memo:
                return memo[i,c]

            memo[i,c] = max(nums[i]+dfs(i+2,c),dfs(i+1,c))
            return memo[i,c]

        ret = max(dfs(0,1),dfs(1,0))

        return ret



# What is dfs(i), represents the number of houses that can be maximally robbed at that index

# What is the state at each step, at the current house

# What are the choices at each step, either rob current house or rob the next house

# Base case, if we run out of houses


        