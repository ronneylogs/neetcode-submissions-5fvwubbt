class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        pivot = 0

        while l <= r:
            m = (l + r) // 2

            # Found pivot
            if m > 0 and nums[m] < nums[m - 1]:
                pivot = m
                break

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        l = 0
        r = len(nums) - 1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        
        while l<=r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        

        return -1
