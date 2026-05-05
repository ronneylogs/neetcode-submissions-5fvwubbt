class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = set()

        res = []

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in nums:
                if i not in seen:
                    seen.add(i)
                    path.append(i)
                    backtrack(path)
                    path.pop()
                    seen.remove(i)
                

        
        backtrack([])
        
        return res


        # choices at each step: pick any number other than itself
        # base case: if we run out of space
        