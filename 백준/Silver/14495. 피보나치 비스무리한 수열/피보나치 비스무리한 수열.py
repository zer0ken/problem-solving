import sys
from functools import cache

@cache
def fibonati(n):
    if n <= 3:
        return 1
    return fibonati(n - 1) + fibonati(n - 3)

sys.stdout.write(str(fibonati(int(sys.stdin.readline()))))