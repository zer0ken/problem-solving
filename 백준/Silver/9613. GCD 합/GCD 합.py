import sys
import math

for _ in range(int(sys.stdin.readline())):
    arr = sorted(map(int, sys.stdin.readline().split()[1:]))
    acc = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            acc += math.gcd(arr[i], arr[j])
    sys.stdout.write(f'{acc}\n')