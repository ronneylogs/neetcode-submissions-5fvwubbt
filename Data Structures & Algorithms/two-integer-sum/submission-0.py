class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res_map = {}
        ret = []

        for i in range(len(nums)):
            kek = target - nums[i]
            if kek not in res_map:
                res_map[nums[i]] = i
            else:
                ret.append(res_map[kek])
                ret.append(i)
                return ret
        return



        # Hashmap way
        