import sys

a, b, c = sorted(map(int, sys.stdin.readline().split()))
if a + b <= c:
    c = a + b - 1
sys.stdout.write(str(a + b + c))