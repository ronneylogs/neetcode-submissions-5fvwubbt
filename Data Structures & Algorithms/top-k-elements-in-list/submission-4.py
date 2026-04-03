class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for i in nums:
            count[i] += 1

        arr = [[] for i in range(len(nums)+1)]

        # print(arr)

        for key,v in count.items():
            arr[v].append(key)
    
        res = []
        print(arr)
        for i in range(len(nums),0,-1):
            print(i)
            for j in arr[i]:
                res.append(j)
                print(res,len(res),k)
                if len(res) >= k:
                    return res
                
        

        


     
        
        # Bucket sort
        # Create n buckets, grouping #s based on their frequencies from 1 to n
        
        # Steps
        # Create freq map that counts how many times each # appears
        # Create groups freq where freq[i] stores all #s that appears i times
        # Iterate from the max of the list until k is satisfied