import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

def dfs(n):
    if n > B:
        return -1
    if n == B:
        return 1
    
    double = dfs(n * 2)
    one = dfs(10 * n + 1)
    
    if double == one == -1:
        return -1
    if double == -1:
        return one + 1
    if one == -1:
        return double + 1
    return min(one, double) + 1

sys.stdout.write(str(dfs(A)))