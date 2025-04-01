import sys
import heapq

results = []
for x in map(int, sys.stdin.read().split()[:-1]):
    divisors = {1}
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            divisors |= {i, x // i}
    
    if sum(divisors) != x:
        results.append(f'{x} is NOT perfect.')
    else:
        results.append(f'{x} = {" + ".join(map(str, sorted(divisors)))}')
sys.stdout.write('\n'.join(results))