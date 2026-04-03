class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dfs(i):
            # Base
            if i>=len(cost):
                return 0
            
            return cost[i] + min(dfs(i+1),dfs(i+2))
        return min(dfs(0),dfs(1))
        




    # IDEA:
    # Base Case:
        # when we are just pass the last index

    # Choices each time
        # Take one step or take two steps
        # Each time we have to consider current cost
