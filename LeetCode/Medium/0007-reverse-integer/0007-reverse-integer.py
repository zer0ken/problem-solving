class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x > 0:
            ret = int(str(x)[::-1])
            return ret if ret <= 2**31 - 1 else 0
        if x < 0:
            ret = -int(str(-x)[::-1])
            return ret if ret >= -(2**31) else 0