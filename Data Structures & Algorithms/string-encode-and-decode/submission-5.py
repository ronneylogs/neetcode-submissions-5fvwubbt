class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            length = len(s)
            ret += str(length)
            ret += "#"
            ret += s
        return ret


    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i=0
        number = ""
        while i <len(s):
            
            # 
            if s[i]!="#":
                number += s[i]

            
            else: 
                num = int(number)
                number =""
                res.append(s[i+1:i+num+1])
                i+=num

            i += 1
        return res

            
