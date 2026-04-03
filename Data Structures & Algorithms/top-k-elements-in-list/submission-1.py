class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        ret = []
        

        for i in nums:
            count_map[i] += 1
        
        freq = [[] for i in range(len(nums)+1)]
        
        for num,cnt in count_map.items():
            freq[cnt].append(num)
        
        print(freq)

        for i in range(len(nums),0,-1):
            for j in range(len(freq[i])):
                ret.append(freq[i][j])
                if len(ret)>=k:
                    return ret
        return ret





        
        # Bucket sort
        # Create n buckets, grouping #s based on their frequencies from 1 to n
        
        # Steps
        # Create freq map that counts how many times each # appears
        # Create groups freq where freq[i] stores all #s that appears i times
        # Iterate from the max of the list until k is satisfied