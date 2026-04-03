class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1

                if l >= r and resLen < (j - i + 1):
                    res = s[i : j + 1]
                    resLen = j - i + 1
        return res



        # Idea is to iterate through every character, for each character, increment left and right pointers
        # and check if they are palindrome each time until it's not a palindrome or we go out of bounds
        # each time collecting the length for the max length

        # Define a function to check if something is palindrome