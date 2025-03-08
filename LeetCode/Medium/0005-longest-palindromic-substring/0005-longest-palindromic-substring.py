class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_palindrome = None
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r <= len(s):
                if s[l] == s[r-1]:
                    l -= 1
                    r += 1
                else:
                    break
            l += 1
            r -= 1
            len_ = r - l
            if max_len < len_:
                max_len = len_
                max_palindrome = (l, r)
            
            if i == len(s) - 1:
                break

            l = i
            r = i + 2
            while l >= 0 and r <= len(s):
                if s[l] == s[r-1]:
                    l -= 1
                    r += 1
                else:
                    break
            l += 1
            r -= 1
            len_ = r - l
            if max_len < len_:
                max_len = len_
                max_palindrome = (l, r) 
        l, r = max_palindrome
        return s[l:r]