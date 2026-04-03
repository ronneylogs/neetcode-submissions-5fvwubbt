class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        # print(count)

        freq = [[] for i in range(len(nums) + 1)]

        for num,cnt in count.items():
            freq[cnt].append(num)

        # print(freq)
        need = k
        res = []
        for i in range(len(nums),0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == need:
                    return res

        
        # Bucket sort
        # Create n buckets, grouping #s based on their frequencies from 1 to n
        
        # Steps
        # Create freq map that counts how many times each # appears
        # Create groups freq where freq[i] stores all #s that appears i times
        # Iterate from the max of the list until k is satisfied