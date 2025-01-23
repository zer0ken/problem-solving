import sys
readline = sys.stdin.readline
n = int(readline().rstrip())

arr = [readline().split() for _ in range(n)]
arr = sorted(arr, key=lambda x: int(x[0]))
for age, name in arr:
    sys.stdout.write(f'{age} {name}\n')