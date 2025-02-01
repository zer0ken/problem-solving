import sys

encoding = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N, B = map(int, sys.stdin.readline().split())

max_exp = 0
while (B ** max_exp) <= N:
    max_exp += 1
max_exp -= 1

for exp in range(max_exp, -1, -1):
    sys.stdout.write(encoding[N // (B ** exp)])
    N %= B ** exp