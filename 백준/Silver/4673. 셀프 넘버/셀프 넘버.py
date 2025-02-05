import sys

def d(n):
    return n + sum(map(int, str(n)))

sieve = [False] * 10001

for n in range(1, 10000):
    if sieve[n]:
        continue
    sys.stdout.write(str(n))
    sys.stdout.write('\n')
    while (n := d(n)) <= 10000:
        sieve[n] = True