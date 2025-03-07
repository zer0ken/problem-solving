class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_palindrome = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                ss = s[i:j]
                if max_len < len(ss) and ss == ss[::-1]:
                    max_len = len(ss)
                    max_palindrome = ss
        return max_palindrome