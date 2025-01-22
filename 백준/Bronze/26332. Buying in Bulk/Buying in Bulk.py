import sys

readline = sys.stdin.readline
t = int(readline().rstrip())
for _ in range(t):
    count, cost = map(int, readline().split())
    total_cost = cost * count - 2 * (count - 1)
    sys.stdout.write(f'{count} {cost}\n{total_cost}\n')