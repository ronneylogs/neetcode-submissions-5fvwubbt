class Solution:
   def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, cur, total):
            # base cases
            if total == target:
                res.append(cur.copy())
                return
            if start>=len(nums) or total > target:
                return


            # Technique 1
            cur.append(nums[start])
            dfs(start, cur, total + nums[start])
            cur.pop()
            dfs(start+1, cur, total)

            # Technique 2
            # explore all candidates starting at index `start`
            # for i in range(start, len(nums)):
            #     cur.append(nums[i])
            #     dfs(i, cur, total + nums[i])   # i not i+1 because we can reuse nums[i]
            #     cur.pop()

        dfs(0, [], 0)
        return res


            




        
        