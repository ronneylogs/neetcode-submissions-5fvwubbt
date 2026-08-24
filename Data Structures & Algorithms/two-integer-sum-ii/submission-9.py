class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l<r:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l+1,r+1]
            elif summ > target:
                r -= 1
            else:
                l += 1
        
        return -1



# input: a sorted array
# the index of two numbers in the sorted array that add up to target number
# Approach: use two pointer method, and decrement / increment based on > or < from targer number
    # case
        # sum > target: decrement r pointer
        # sum < taget: increment l pointer
        # sum == target: return target