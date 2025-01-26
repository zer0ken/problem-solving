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

is_nn_square = [True] * (max_ - min_ + 1)

for prime in primes:
    square = prime * prime
    k = min_ // square
    if min_ % square != 0:
        k += 1
    
    for k_square in range(square * k, max_ + 1, square):
        is_nn_square[k_square - min_] = False

sys.stdout.write(str(sum(is_nn_square)))