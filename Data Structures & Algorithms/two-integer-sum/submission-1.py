class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}

        for i in range(len(nums)):
            if nums[i] in diff_map:
                return [diff_map[nums[i]],i]
            diff_map[target-nums[i]] = i
       
       
        return []
       
        # Hashmap to store differences
        # if the number doesn't exist in the hashmap
            # We add the target - number = difference
                # Store into hashmap like so (key,val) -> (difference,index of number)
        # the number exists
            # We add the current index and the val to our res and return
        