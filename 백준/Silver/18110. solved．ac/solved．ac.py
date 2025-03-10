import sys

readline = sys.stdin.readline

n = int(readline().rstrip())
if n == 0:
    sys.stdout.write('0')
else:
    arr = sorted(int(readline().rstrip()) for _ in range(n))
    cut = int(n * 0.15 + 0.5)
    if cut > 0:
        arr = arr[cut:-cut]
        n -= 2 * cut
    sys.stdout.write(str(int(sum(arr) / n + 0.5)))