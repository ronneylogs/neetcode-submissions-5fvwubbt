class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def findMin(n: List[int]) -> int:

            l = 0
            r = len(n)-1

            while l<r:
                m = (l+r)//2

                if n[m] < n[r]:
                    r = m
                else:
                    l = m + 1

            return l

        def binarySearch(n,target):
            print(n)
            l = 0
            r = len(n)-1

            while l<=r:
                m = (l+r) // 2
                print(m)
                if n[m] == target:
                    return m
                elif n[m] < target:
                    l = m+1
                else:
                    r = m-1
            
            return -1
        

        mine = findMin(nums)

        res1 = binarySearch(nums[0:mine],target)
        res2 = binarySearch(nums[mine:],target)

        print(mine)
        print(res1)
        print(res2)

        if res1 != -1:
            return res1
        
        if res2 != -1:
            return res2+mine
        
        return -1


        




    # Idea is that we want to shrink towards the smallest value
    # We are finding the lower bound
        