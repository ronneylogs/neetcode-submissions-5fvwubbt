class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res_set = set()


        for i in range(len(nums)):
            anchor = i
            l = i + 1
            r = len(nums)-1
            while(l<r):
                if nums[l]+nums[r]+nums[i] > 0 :
                    r = r - 1
                elif nums[l]+nums[r]+nums[i] < 0:
                    l = l + 1
                else:
                    res_set.add((nums[i],nums[l],nums[r]))
                    l = l + 1
                    r = r - 1
                
        return list(res_set)





        



        