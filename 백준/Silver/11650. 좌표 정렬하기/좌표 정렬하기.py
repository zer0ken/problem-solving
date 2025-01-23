import sys
readline = sys.stdin.readline
n = int(readline().rstrip())

arr = [tuple(map(int, readline().split())) for _ in range(n)]
arr = sorted(arr, key=lambda x: x[1])
arr = sorted(arr, key=lambda x: x[0])

for x, y in arr:
    sys.stdout.write(f'{x} {y}\n')