import sys

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

for _ in range(int(sys.stdin.readline())):
    arr = sorted(map(int, sys.stdin.readline().split()[1:]))
    acc = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            acc += gcd(min(arr[i], arr[j]), max(arr[i], arr[j]))
    sys.stdout.write(f'{acc}\n')