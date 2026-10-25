class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            length = len(s)
            ret += "#"
            ret += str(length)
            ret += "#"  # Added delimiter
            ret += s
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0

        while i < len(s):
            l = 0

            if s[i] == "#":
                i += 1

                # Find where the length ends
                j = i
                while s[j] != "#":
                    j += 1

                l = int(s[i:j])

                # Move i to the end of the length
                i = j

                ret.append(s[i+1:i+l+1])

            i = i + l + 1

        return ret