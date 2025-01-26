import sys
import math

min_, max_ = map(int, sys.stdin.readline().split())

max_sqrt = int(max_ ** 0.5)

# prime under max_sqrt
primes = [i for i in range(max_sqrt + 1)]
for i in range(2, max_sqrt + 1):
    if primes[i] == 0:
        continue
    for j in range(i*2, max_sqrt + 1, i):
        primes[j] = 0
primes = set(primes[2:])
if 0 in primes:
    primes.remove(0)

# 0: min_, -1: max_
is_nn_square = [True] * (max_ - min_ + 1)
count = max_ - min_ + 1

for sqrt in primes:
    temp_sq = sqrt * sqrt
    k = math.ceil(min_ / temp_sq)
    sq = temp_sq * k
    
    for sq in range(temp_sq * k, max_ + 1, temp_sq):
        if is_nn_square[sq - min_]:
            is_nn_square[sq - min_] = False
            count -= 1

sys.stdout.write(str(count))