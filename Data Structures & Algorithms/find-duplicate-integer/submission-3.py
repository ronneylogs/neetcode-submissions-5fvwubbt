class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for n in nums:
            idx = abs(n) - 1
            if nums[idx] < 0:
                return abs(n)
            nums[idx] *= -1


        return -1
        

        # 1. Go through each number and mark it's index position as -1
        # 2. if we encoutner the number again it should be neg
        