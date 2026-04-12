class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l<r:
            m = (l+r) // 2

            if nums[m] >= nums[-1]:
                l = m+1
            else:
                r = m
        


        return nums[l]
        # if nums[m] >= last item, answer on the right of m
        # otherwise answer should be on the left or equal to m

