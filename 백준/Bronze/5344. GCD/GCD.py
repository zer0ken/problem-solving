import sys

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write(f'{gcd(min(a, b), max(a, b))}\n')