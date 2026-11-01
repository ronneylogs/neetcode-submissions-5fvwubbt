class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)

        for i in range(len(nums)):
            count[nums[i]] += 1
        
        arr = [[] for i in range(len(nums)+1)]

        for value,times in count.items():
            arr[times].append(value)


        res = []

        for i in range(len(arr)-1,0,-1):
            for items in arr[i]:
                res.append(items)
                if len(res) == k:
                    return res


        return []
                





        


        # Given an array and also a k
        # We want the top k elements repeated in the array

        # For each number in the array, count how many times it has been repeated.
        # Based on how many times it has been repeated create an array of arrays, were the position is how many times it was repeated, and the items inside are the repeated items


        # At the end, we just loop through the outer array from back to front to grab the items into the res array, stopping when we are full and returning it