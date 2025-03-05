class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        p1 = 0
        p2 = 1
        max_len = 1
        while p2 < len(s):
            if s[p2] not in s[p1:p2]:
                p2 += 1
                l = p2 - p1
                if max_len < l:
                    max_len = l
            else:
                p1 += 1
        return max_len