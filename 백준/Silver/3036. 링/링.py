import sys

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = arr[0]
for y in arr[1:]:
    gcd_ = gcd(min(x, y), max(x, y))
    sys.stdout.write(f'{x // gcd_}/{y // gcd_}\n')