class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums.sort()

        # Outer for loop for each index
        for i in range(len(nums)):
            value = nums[i]
            l = i+1
            r = len(nums) - 1
        
            # while loop for two pointer part
            while l<r:
      
                total = value + nums[l] + nums[r]

                if total == 0:
                    tmp = [value,nums[l],nums[r]]
                    tmp.sort()
                    if tuple(tmp) not in ret:
                        ret.add(tuple(tmp))
                    l += 1
                    r -= 1
                elif total<0:
                    l += 1
                else:
                    r -= 1


        return [list(item) for item in ret]

    

    # Sorting: O(nlogn)

    # Algorithm O(n) * O(n)