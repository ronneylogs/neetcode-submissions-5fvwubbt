class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for i in range(len(strs)):
            sort = "".join(sorted(strs[i]))
            m[sort].append(i)
        
        res = []

        for k,v in m.items():
            l = []
            for w in v:
                l.append(strs[w])
            res.append(l)

        return res


