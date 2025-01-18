import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    even_numbers = list(filter(lambda x: x % 2 == 0, map(int, sys.stdin.readline().split())))
    sys.stdout.write(f'{sum(even_numbers)} {min(even_numbers)}\n')