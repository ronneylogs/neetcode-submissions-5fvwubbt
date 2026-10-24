class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        c = defaultdict(int)

        for i in range(len(nums)):
            c[nums[i]] += 1
    
        l = [[] for i in range(len(nums)+1)]

        for key,v in c.items():
            l[v].append(key)

        res = []

        for i in range(len(nums),0,-1):
            for j in l[i]:
                res.append(j)
                if len(res) >= k:
                    return res