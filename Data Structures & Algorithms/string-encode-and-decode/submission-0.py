class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        res = ""
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ","
        res += "#"
        for s in strs:
            res += s
        return res

# What do we have at this point
# res = "4,4#leetcode"
    def decode(self, s: str) -> List[str]:
        sizes,res,i = [],[],0

        while s[i] != "#":
            cur = ""

            # For in cases where the word itself is longer than 10 or more
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i+sz])
            i += sz
        return res





