import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    sys.stdout.write(' ' * (N - i) + '*' * (i * 2 - 1) + '\n')
for i in range(N - 1, 0, -1):
    sys.stdout.write(' ' * (N - i) + '*' * (i * 2 - 1) + '\n')