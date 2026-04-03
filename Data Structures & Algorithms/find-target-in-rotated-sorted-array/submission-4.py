class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l

        def binary_search(l,r,target):
            
            while l<=r:
                m = (l+r) // 2

                if nums[m]==target:
                    return m

                if nums[m] > target:
                    r = m - 1
                
                if nums[m] < target:
                    l = m + 1
                
            return -1
        
        leftSide = binary_search(0,pivot-1,target)
        print(leftSide)
        if (leftSide != -1):
            return leftSide
        
        rightSide = binary_search(pivot,len(nums)-1,target)
        print(rightSide)
        if (rightSide != -1):
            return rightSide
        
        return -1
        


    


    # Key idea
    # Find the pivot
        # After pivot is found, we can just run regular binary search on either part