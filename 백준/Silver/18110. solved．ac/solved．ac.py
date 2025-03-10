import sys

n, *arr = map(int, sys.stdin.read().split())
if n == 0:
    sys.stdout.write('0')
else:
    arr.sort()
    cut = int(n * 0.15 + 0.5)
    if cut > 0:
        arr = arr[cut:-cut]
        n -= 2 * cut
    sys.stdout.write(str(int(sum(arr) / n + 0.5)))