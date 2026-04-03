class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        prev = 0
        tmp = nums
        tmp.sort()
        for i in tmp:
            if i == prev:
                return i
            prev = i



        

        # Input: array of integers
        # Output: an integer of the repeated number
        # Idea:
        # Loop through the array and if the next num === current num, return num