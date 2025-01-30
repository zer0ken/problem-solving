import sys
N, M = map(int, sys.stdin.readline().split())

if M <= 26:
    order = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[M-1]
else:
    order = 'abcdefghijklmnopqrstuvwxyz'[(M - 1) // 26 - 1]
    order += 'abcdefghijklmnopqrstuvwxyz'[(M - 1) % 26]

sys.stdout.write(f'SN {N}{order}')