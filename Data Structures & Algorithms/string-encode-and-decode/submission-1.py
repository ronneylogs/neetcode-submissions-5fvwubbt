class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            length = len(i)
            res = res + str(length) + "#" + i
        
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        number = ""
        while i < len(s):
            if s[i] == "#":
                print(int(number))
                res.append(s[i+1:i+int(number)+1])
                i = i + int(number)
                number = ""
            else:
                number += s[i]
            
            i += 1

        return res









