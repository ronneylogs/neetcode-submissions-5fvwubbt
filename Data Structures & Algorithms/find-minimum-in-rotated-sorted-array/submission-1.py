class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:

            # Middle
            m = (l+r) // 2

            # If middle is smaller than right, then answer is itself or on the left side of array
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]