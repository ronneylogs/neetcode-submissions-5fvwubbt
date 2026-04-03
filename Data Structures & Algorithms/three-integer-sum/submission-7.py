class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1

            while(l<r):
                if(nums[i]+nums[l]+nums[r]==0):
                    res.add((nums[i],nums[l],nums[r]))
                    l = l+1
                    r = r-1
                    
                
                elif(nums[i]+nums[l]+nums[r]>0):
                    r = r -1
                
                else:
                    l = l+1

        return list(res)
            





        # Steps:
        # 1. Sort all items so smallest on left, largest on right
        # 2. Walk through the array, have a L and R pointer and increment





        



        