class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x > 0:
            return int(str(x)[::-1])
        if x < 0:
            return -int(str(-x)[::-1])