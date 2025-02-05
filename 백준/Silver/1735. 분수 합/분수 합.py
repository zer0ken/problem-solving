import sys

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

a1, b1, a2, b2 = map(int, sys.stdin.read().split())
a = a1 * b2 + a2 * b1
b = b1 * b2
gcd_ = gcd(min(a, b), max(a, b))
sys.stdout.write(f'{a // gcd_} {b // gcd_}')