class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        seen = defaultdict(lambda: False)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                
                return
            
            if len(path) > len(nums):
                return
            
            for i in range(n):
                if not seen[nums[i]]:
                    path.append(nums[i])
                    seen[nums[i]] = True
                    backtrack(path)
                    path.pop()
                    seen[nums[i]] =False
                

            return
        
        backtrack([])

        return res
        
        # idea
        # What are our choices at each call
        # [] then [1] [2] [3] 
            # then [1,2] [1,3] and [2,1] [2,3] and [3,1] [3,2]
                # then [1,2,3] [1,3,2] and [2,1,3] [2,3,1] and [3,1,2] [3,2,1]