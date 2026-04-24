class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    seen.remove(nums[i])
                
            return

        backtrack([])
        return res


    
    # idea
        # at each step our choise is everything, use a seen to keep track of what is already seen
        # base case is if we run out of space 