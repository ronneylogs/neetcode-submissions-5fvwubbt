class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for i in range(len(strs)):
            sort = "".join(sorted(strs[i]))
            m[sort].append(strs[i])

        return list(m.values())


        # Given an array of strings, return an array of array of strings
        # For loop through the input
            # sort it then add to dict {sorted_key:[real word]}

        # return dict.values()
        