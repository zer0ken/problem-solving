import sys
import math

M, N = map(int, sys.stdin.readline().split())

is_prime = [False, False] + [True] * (N - 1)

for i in range(2, N + 1):
    if not is_prime[i]:
        continue
    v = i * 2
    while v <= N:
        if is_prime[v]:
            is_prime[v] = False
        v += i

for i, is_prime in enumerate(is_prime[M:], M):
    if is_prime:
        sys.stdout.write(f'{str(i)}\n')