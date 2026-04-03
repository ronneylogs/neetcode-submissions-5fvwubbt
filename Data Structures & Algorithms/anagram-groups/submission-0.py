class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        print(res)

        for i in strs:
            sortedS = "".join(sorted(i))
            res[sortedS].append(i)
        
        return list(res.values())

        # Sort the items, then insert as a string in dictionary
        # Dictionary key: sorted word, value:[array of words that ara anagrams]