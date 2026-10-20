class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for i in range(len(strs)):
            sort = "".join(sorted(strs[i]))
            m[sort].append(strs[i])
        
        return list(m.values())


