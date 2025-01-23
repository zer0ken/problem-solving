import sys
from collections import Counter

readline = sys.stdin.readline
t = int(readline().rstrip())
for _ in range(t):
    n = int(readline().rstrip())
    yjjs = [tuple(readline().split()) for __ in range(n)]
    best_yjj = max(yjjs, key=lambda yjj: int(yjj[1]))
    sys.stdout.write(f'{best_yjj[0]}\n')