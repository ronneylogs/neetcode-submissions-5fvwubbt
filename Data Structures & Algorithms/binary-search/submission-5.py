class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1

        while l<r:
            m = (l+r) // 2
            if nums[m]<target:
                l = m+1
            else:
                r = m
            
        if nums[l] == target:
            return l
        else:
            return -1





        