class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        i = 0
        if s and s[0] in '-+':
            ss = s[0] + '0'
            i = 1
        else:
            ss = '+0'
        for i in range(i, len(s)):
            if s[i] not in '0123456789':
                break
            ss += s[i]
        ret = int(ss)
        return min(max(ret, -(2**31)), 2**31 - 1)