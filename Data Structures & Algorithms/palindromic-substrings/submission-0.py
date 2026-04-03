class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0

        # Odd length, ex "asa"
        for i in range(len(s)):
            l = i
            r = i
            while l >=0 and r < len(s) and s[l]==s[r]:
                l = l - 1
                r = r + 1 
                res += 1


        # Even length ex "assa"
        for i in range(len(s)):
            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                l = l-1
                r = r+1
                res += 1
        return res


