class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        pivot = 0

        # handle not rotated
        if nums[0] > nums[-1]:
            while l <= r:
                mid = (l + r) // 2

                if mid > 0 and nums[mid] < nums[mid - 1]:
                    pivot = mid
                    break

                if mid < n - 1 and nums[mid] > nums[mid + 1]:
                    pivot = mid + 1
                    break

                if nums[mid] >= nums[0]:
                    l = mid + 1
                else:
                    r = mid - 1

        # reset bounds for actual binary search
        l, r = 0, n - 1

        # decide which half to search using correct boundary nums[-1]
        if nums[pivot] <= target <= nums[-1]:
            l = pivot
        else:
            r = pivot - 1

        # normal binary search
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1
