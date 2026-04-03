class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i



        # Two numbers added to make the target
        # Hashmap to store numbers that have been visited
            # k: the number, v: the index
        # For each #, we check
            # Calculate the difference
            # if it's in the hashmap, we return the cur index and the value in the hashmap
            # otherwise we add it ot the hashmap
        