import sys
n = int(input())
for _ in range(n):
    a, b = sys.stdin.readline().split()
    sys.stdout.write(f'{abs(float(a) - float(b)):.1f}\n')