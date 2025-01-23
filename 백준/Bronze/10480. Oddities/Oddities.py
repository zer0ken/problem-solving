import sys

readline = sys.stdin.readline
t = int(readline().rstrip())
for _ in range(t):
    x = int(readline().rstrip())
    odd = x % 2
    sys.stdout.write(f'{x} is {"odd" if odd else "even"}\n')