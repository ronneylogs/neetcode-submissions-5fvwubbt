class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        res = []

        for i in nums:
            count[i] += 1
        
        freq = [[] for i in range(len(nums)+1)]
        for number,cnt in count.items():
            freq[cnt].append(number)
        
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)>=k:
                    return res
        
        return res


        

        
        # Bucket sort
        # Create n buckets, grouping #s based on their frequencies from 1 to n
        
        # Steps
        # Create freq map that counts how many times each # appears
        # Create groups freq where freq[i] stores all #s that appears i times
        # Iterate from the max of the list until k is satisfied