class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        for string in strs:
            length = str(len(string))
            newStr += length
            newStr += "#"
            newStr+=string
        return newStr


    def decode(self, s: str) -> List[str]:
        number = ""
        res = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                num = int(number)
                number = ""
                res.append(s[i+1:i+1+num])
                i+=num
                

            else: number += s[i]

            i += 1
        return res
            
     








