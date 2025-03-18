import sys
import math

L, A, B, C, D = map(int, sys.stdin.read().rstrip().split())
print(L - max(math.ceil(A / C), math.ceil(B / D)))